from django.urls import path
from . import views




urlpatterns = [
    path('inicio/', views.index),
    path('vista2/', views.pagina2)

]