from django.urls import path

from .controller import views

app_name = 'mongo_module'
urlpatterns = [
    path('', views.index, name='index'),
    path('user/', views.checkAllUsers, name='checkAllUsers'),
    path('register/', views.register, name='register'),
    path('user/<str:user_id>/', views.searchUser, name='searchUser'),
    path('notes/', views.notes, name='notes'),
    path('note/add/', views.addNote, name='addNote'),
]
