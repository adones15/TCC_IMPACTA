from django.urls import path
from .views import login, produto, confirmacaoCadastroProduto, cadastro_funcionario, autenticar_funcionario
from django.urls import include

urlpatterns = [
    path('', login, name='login'),
    path('produto', produto, name='produto'),
    path('confirmacao-cadastro-produto/', confirmacaoCadastroProduto, name='confirmacao-cadastro-produto'),
    path('cadastro_funcionario', cadastro_funcionario, name ='cadastro_funcionario'),
    path('autenticar_funcionario', autenticar_funcionario, name='autenticar_funcionario')
]