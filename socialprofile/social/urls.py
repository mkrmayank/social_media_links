from django.contrib import admin
from django.urls import path
from social import views

urlpatterns = [
    path('', views.index, name='home'),
    path('register', views.register, name='register'),

]