from . import views
from django.urls import path, include

urlpatterns = [
    path('equipe_atual', views.equipe, name="equipe_atual"),
    path('ex_membros', views.ex_membros, name="ex_membros"),
    path('team', views.team, name='team'),
    path('former', views.former, name="former")
    ]
