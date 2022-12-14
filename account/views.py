from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from .forms import AuthUserForm, RegUserForm
from users.models import CustomUser
from main.models import Link


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


class BlogProfileView(DetailView):
    model = CustomUser
    context_object_name = 'profile'
    template_name = 'account/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_links'] = Link.objects.filter(user_id=context['object'].id)
        return context
