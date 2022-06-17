from django.urls import path

#Instanciamos a "views.py" dentro de nuestra app
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]