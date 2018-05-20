from django.urls import path
from . import views

urlpatterns = [
    path('say/<str:words>', views.say520, name='say520')
]
