from django import forms
from authapp.models import ShopUser
from authapp.forms import ShopUserEditForm, ShopUserRegisterForm
from mainapp.models import Product


class ShopUserAdminEditForm(ShopUserEditForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'email', 'age', 'avatar', 'is_staff', 'is_active')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name in ['is_staff', 'is_active', 'avatar']:
                field.widget.attrs['class'] = 'form-control col-3'
            else:
                field.widget.attrs['class'] = 'form-control col-5'



class ShopUserAdminRegisterForm(ShopUserRegisterForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'email', 'age', 'avatar', 'is_staff', 'is_active')


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control col-5'


class UploadFileForm(forms.Form):
    file = forms.FileField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control form-control-sm col-3'
            field.help_text = ''

