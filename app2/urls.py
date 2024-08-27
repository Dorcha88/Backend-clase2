from django.urls import path
from . import views




urlpatterns = [
    path('inicio/', views.index),
    path('inicio2/', views.vista2)

]