from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.user_logging_in, name='login'),
    path('signup/', views.sign_up_view, name='signup'),
    path('logout/', views.user_logging_out, name='logout')
    ]