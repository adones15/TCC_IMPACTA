from django.urls import path
from .views import login, produto
from django.urls import include

urlpatterns = [
    path('', login, name='login'),
    path('produto', produto, name='produto')
]