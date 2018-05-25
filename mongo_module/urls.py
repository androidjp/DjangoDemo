from django.urls import path
from . import views

app_name = 'mongo_module'
urlpatterns = [
    path('', views.index, name='index'),
    path('user/', views.checkAllUsers, name='checkAllUsers'),
    path('register/', views.register, name='register'),
    path('user/<str:user_id>/', views.searchUser, name='searchUser'),
]
