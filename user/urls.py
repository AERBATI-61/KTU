from django.contrib import admin
from django.urls import path

from user.views import *

urlpatterns = [
    path('login/', loginUser, name='login'),
    path('loginout/', logoutUser, name='logout'),
    path('register/', register, name='register'),
]
