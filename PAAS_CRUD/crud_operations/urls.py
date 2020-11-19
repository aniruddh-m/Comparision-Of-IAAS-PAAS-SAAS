from django.urls import path
from . import views

app_name = 'crud_operations'

urlpatterns = [
    path('Create', views.Create, name='Create'),
    path('Update', views.Update, name='Update'),
    path('Delete', views.Delete, name='Delete'),
    path('Retrieve', views.Retrieve, name='Retrieve'),
    path('', views.index, name='index')
]