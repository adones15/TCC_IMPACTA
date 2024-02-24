from django.urls import path
from .views import login, produto, confirmacaoCadastroProduto
from django.urls import include

urlpatterns = [
    path('', login, name='login'),
    path('produto', produto, name='produto'),
    path('confirmacao-cadastro-produto/', confirmacaoCadastroProduto, name='confirmacao-cadastro-produto')
]