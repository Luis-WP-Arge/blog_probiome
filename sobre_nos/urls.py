from . import views
from django.urls import path, include

urlpatterns = [
    path('sobre_nos', views.sobre_nos, name="sobre_nos"),
    path('about_us', views.about_us, name="about_us")
    ]

