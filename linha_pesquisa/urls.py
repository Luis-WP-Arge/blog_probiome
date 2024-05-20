from . import views
from django.urls import path, include

urlpatterns = [
    path('setaria/', views.linha_setaria, name="setaria"),
    path('gossypium/', views.linha_gossypium, name="gossypium"),
]