from django.urls import path
from .views import produto
from django.urls import include

urlpatterns = [
    path('produto', produto, name='produto')
]