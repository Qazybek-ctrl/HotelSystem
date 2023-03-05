from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from .forms import UserRegisterForm


class UserRegisterView(CreateView):
    template_name = 'Auth/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
        

class LoginingView(LoginView):
    template_name = 'Auth/login.html'
    form_class = AuthenticationForm

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'login_form': form})
