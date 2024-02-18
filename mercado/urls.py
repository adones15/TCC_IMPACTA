from django.urls import path
from .views import pag_inicial
from django.urls import include

urlpatterns = [
    path('', pag_inicial, name='pag_inicial')
]