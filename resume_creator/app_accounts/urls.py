
from django.contrib import admin
from django.urls import path , include
from app_accounts import views



app_name = 'app_accounts'

urlpatterns = [
    path("signup/", views.SignUpView, name="signup")
    ]
