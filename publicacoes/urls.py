from . import views
from django.urls import path, include

urlpatterns = [
    path('publicacoes', views.publicacoes, name="publicacoes")
    ]
