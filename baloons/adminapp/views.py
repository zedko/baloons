from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from adminapp.forms import ShopUserAdminEditForm, ShopUserAdminRegisterForm, ProductUpdateForm, UploadFileForm
from authapp.models import ShopUser
from mainapp.models import Product, ProductCategory
from basketapp.models import Basket
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.edit import CreateView, UpdateView
from django.utils.decorators import method_decorator
from django.http import HttpResponseNotFound
from mainapp.management.commands.xls_import import xls_import_products


def get_model_by_string(string):
    if string == 'product':
        model = Product
    elif string == 'user':
        model = ShopUser
    elif string == 'category':
        model = ProductCategory
    elif string == 'basket':
        model = Basket
    else:
        return HttpResponseNotFound()
    return model


# ShopUser CRUD (delete is common for all models)
@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    title = 'пользователи | создание'
    if request.method == 'POST':
        user_form = ShopUserAdminRegisterForm(request.POST, request.FILES)
        if user_form.is_valid:
            user_form.save()
            return HttpResponseRedirect(reverse('admin2:users'))
    else:
        user_form = ShopUserAdminRegisterForm()

    content = {
        'title': title,
        'update_form': user_form,
    }
    return render(request, 'adminapp/user_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def users_read(request):
    title = 'users'
    content = {
        'title': title,
        'user_objects': ShopUser.objects.all().order_by('username')
    }
    return render(request, 'adminapp/users.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_update(request, pk):
    title = 'пользователи | редактирование'
    edit_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        user_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)
        if user_form.is_valid:
            user_form.save()
            return HttpResponseRedirect(reverse('admin2:user_update', args=[edit_user.pk]))
    else:
        user_form = ShopUserAdminEditForm(instance=edit_user)

    delete_url = f'/admin2/delete?obj=user&pk={pk}'
    content = {
        'title': title,
        'update_form': user_form,
        'delete_url': delete_url
    }

    return render(request, 'adminapp/user_update.html', content)


# Product CRUD (delete is common for all models)
class ProductCreateView(CreateView):
    model = Product
    template_name = 'adminapp/create.html'
    success_url = reverse_lazy('admin2:users')
    form_class = ProductUpdateForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'продукты | создание'
        return context


def products(request, pk_cat):
    category = get_object_or_404(ProductCategory, pk=pk_cat)
    title = f'All products in {category.name}'
    products_list = Product.objects.filter(category__pk=pk_cat).order_by('name')
    content = {
        'title': title,
        'category': category,
        'products': products_list,
    }
    return render(request, 'adminapp/products.html', content)


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'adminapp/create.html'
    form_class = ProductUpdateForm

    def get_success_url(self):
        success_url = self.request.path
        return success_url

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    # TODO find out how to form get params in URLs to make a proper link delete_confirm.html
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['delete_url'] = f'/admin2/delete?obj=product&pk={self.object.pk}'
        return context


# ProductCategory CRUD (delete is common for all models)
class CategoryCreateView(CreateView):
    model = ProductCategory
    template_name = 'adminapp/create.html'
    fields = '__all__'
    success_url = reverse_lazy('admin2:categories')


@user_passes_test(lambda u: u.is_superuser)
def categories_read(request):
    title = "Categories"
    all_cats = ProductCategory.objects.all().order_by('name')
    content = {
        'title': title,
        'categories': all_cats,
    }
    return render(request, 'adminapp/categories.html', content)


class CategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'adminapp/create.html'
    fields = ['id', 'name', 'description']
    success_url = reverse_lazy('admin2:categories')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['delete_url'] = f'/admin2/delete?obj=category&pk={self.object.pk}'
        return context


# TODO basket view
@user_passes_test(lambda u: u.is_superuser)
def basket_read(request):
    pass


@user_passes_test(lambda u: u.is_superuser)
def basket_delete(request, pk):
    pass


# TODO add xlsx import logic and template
@user_passes_test(lambda u: u.is_superuser)
def xlsx_import(request):
    title = "XLSX import"
    context = {
        'title': title,
    }
    if request.method == 'GET' or not request.FILES:
        form = UploadFileForm()
        context['file_upload_form'] = form
        return render(request, 'adminapp/xls_import.html', context)
    if request.method == 'POST' and request.FILES['file']:
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print('ok')
            file = form.cleaned_data['file']
            xls_import_products(file)
            print('ok second')
            context['success'] = True
            return render(request, 'adminapp/xls_import.html', context)




@user_passes_test(lambda u: u.is_superuser)
def delete(request):
    """
    delete confirmation logic for every model
    pass request.GET params obj[str], pk[int]
    """
    if request.method == 'GET':
        obj_type = request.GET['obj']
        model = get_model_by_string(obj_type)
        obj = get_object_or_404(model, pk=request.GET['pk'])
        title = f'Confirm deletion of {obj_type} {obj}'

        context = {
            'title': title,
            'object': obj,
            'obj_type': obj_type,
        }
        return render(request, 'adminapp/delete_confirm.html', context)

    if request.method == 'POST':
        model = get_model_by_string(request.POST['model'])
        obj = get_object_or_404(model, pk=request.GET['pk'])
        obj.delete()
        return HttpResponseRedirect(reverse('admin2:users'))