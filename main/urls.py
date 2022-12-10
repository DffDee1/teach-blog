from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add_video', views.add_video, name='add_vid'),
    path('account/', include('account.urls'))
]
