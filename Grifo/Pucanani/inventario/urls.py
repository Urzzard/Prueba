from django.urls import path
from . import views

urlpatterns = [
    path('', views.new),
    path('inventario/', views.inventario)
]
