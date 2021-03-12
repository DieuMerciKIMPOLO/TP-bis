from django.urls import path
from . import views

app_name = 'gestioncontainers'
urlpatterns = [
    path('formulaire/', views.traitement, name='index'),
]