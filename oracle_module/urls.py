from django.urls import path

from . import views

app_name = 'oracle_module'
urlpatterns = [
    path('customers/', views.showCustomers, name='showCustomers'),
    path('customers/add/', views.addCustomer, name='addCustomer'),
]
