from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login', views.BlogLoginView.as_view(), name='account_login'),
    path('register', views.BlogRegisterView.as_view(), name='account_register'),
    path('logout', views.LogoutView.as_view(), name='account_logout')
]
