from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from accounts import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'
urlpatterns = [

    path('register/', views.register, name = "register"),
    #Django Auth
    path('login/', views.login, name = "login"),
    path('logout/', views.logout, name = "logout"),
]
