from django.urls import path

from django.contrib.auth.views import LoginView

from .views import homePage

urlpatterns = [
    path('', homePage, name='home')
]