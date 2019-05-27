from django.urls import path
from . import views


urlpatterns = [
    path('', views.ana_sayfa, name='ana_sayfa'),
]