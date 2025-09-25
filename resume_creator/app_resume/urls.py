from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app_resume import views

app_name = 'app_resume'

urlpatterns = [
    path('', views.index),
    path('resume', views.resume, name="resume"),
    path('edit', views.edit, name="edit"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
