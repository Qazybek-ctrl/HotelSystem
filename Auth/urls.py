from django.urls import path

from django.contrib.auth.views import LoginView, LogoutView

from .views import LoginingView, UserRegisterView

urlpatterns = [
    path('login/', LoginingView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]