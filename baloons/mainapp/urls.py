from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
   path('<int:url_key>/', mainapp.product_page, name='product'),
]