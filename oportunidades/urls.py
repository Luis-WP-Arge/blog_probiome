from . import views
from django.urls import path, include

urlpatterns = [
    path('oportunidades', views.oportunidades, name="Oportunidades")
    ]
