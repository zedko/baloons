from django.urls import path, re_path

import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('users/', adminapp.users_read, name='users'),
    path('users/create/', adminapp.user_create, name='user_create'),
    path('users/update/<int:pk>/', adminapp.user_update, name='user_update'),


    path('categories/create/', adminapp.CategoryCreateView.as_view(), name='category_create'),
    path('categories/read/', adminapp.categories_read, name='categories'),
    path('categories/update/<int:pk>', adminapp.CategoryUpdateView.as_view(), name='category_update'),


    path('products/create/', adminapp.ProductCreateView.as_view(), name='product_create'),
    path('products/read/category/<int:pk_cat>', adminapp.products, name='products'),
    path('products/update/<int:pk>', adminapp.ProductUpdateView.as_view(), name='product_update'),

    re_path(r'^delete$', adminapp.delete, name='delete'),
    path('products/xlsx_import/', adminapp.xlsx_import, name='xlsx_import'),
]

