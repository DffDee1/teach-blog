from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import AuthUserForm, RegUserForm
from users.models import CustomUser


class BlogLoginView(LoginView):
    template_name = 'account/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return self.success_url


class BlogRegisterView(CreateView):
    model = CustomUser
    template_name = 'account/register.html'
    form_class = RegUserForm
    success_url = reverse_lazy('home')
    success_msg = 'Пользователь успешно создан'

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        auth_user = authenticate(username=username, password=password)
        login(self.request, auth_user)
        return form_valid


class BlogLogoutView(LogoutView):
    next_page = reverse_lazy('home')
