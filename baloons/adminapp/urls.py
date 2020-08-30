from django.urls import path

import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.user_read, name='view'),
    path('add/<int:pk>/', adminapp.user_create, name='add'),
    path('remove/<int:pk>)/', adminapp.user_delete, name='remove'),
    path('edit/<int:pk>/', adminapp.user_update, name='edit'),
]
