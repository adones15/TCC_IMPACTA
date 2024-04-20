from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from .models import Produtos, Funcionarios
from django.shortcuts import render, redirect
from django.contrib import messages

def produto(request):

    if request.method == 'POST':

        id_produto = request.POST.get('id')
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        categoria = request.POST.get('categoria')
        fornecedor = request.POST.get('fornecedor')

        print('##################################: ')
        print('CAIU NO POST: ')
        print(id_produto)
        print('##################################: ')
        
        if(id_produto):
            print('caiu no editar')

            # Recupere o produto existente do banco de dados
            produto = get_object_or_404(Produtos, pk=id_produto)

            # Atualize os dados do produto com os novos valores
            produto.Nome = nome
            produto.Descricao = descricao
            produto.Categoria = categoria
            produto.Fornecedor = fornecedor
            produto.save()

            return redirect('confirmacao-cadastro-produto')

        else:
            # Criar uma nova instância do modelo Produto com os dados do formulário
            novo_produto = Produtos(Nome=nome, Descricao=descricao, Categoria=categoria, Fornecedor=fornecedor)
                
            # Salvar o novo produto no banco de dados
            novo_produto.save()
            # Redirecionar para alguma página, talvez uma página de confirmação
            return redirect('confirmacao-cadastro-produto')
    else:
        print('CAIU NO GET')
        produtos = Produtos.objects.all()

        print('##################################: ')
        print('##################################: ')
        print('PRODUTOS')
        print(produtos)
        #return render(request, "./produto.html")
        return render(request, 'produto.html', {'produtos': produtos})

def confirmacaoCadastroProduto(request):
    return render(request, './confirmacao-cadastro-produto.html')

def login(request):
    return render(request, "./login.html")

def cadastro_funcionario(request):

    # Capturando os valores do formulario e jogando nas variaveis
    nome = request.POST.get('nome')
    cargo = request.POST.get('cargo')
    telefone = request.POST.get('telefone')
    senha = request.POST.get('senha')

    # Criar uma nova instância do modelo Funcionario com os dados do formulário
    novo_funcionario = Funcionarios(Nome=nome, Cargo=cargo, Telefone=telefone, Senha=senha)

    # Salvar o novo funcionario no banco de dados
    novo_funcionario.save()

    # Mensagem de sucesso do cadastro do funcionario
    messages.success(request, 'Funcionário cadastrado com sucesso!')

    # Redirecionar para a página de login
    return redirect('login') 

def autenticar_funcionario(request):

    nome = request.POST.get('nome')
    senha = request.POST.get('senha')

    # Verifica se existe um usuário com o nome fornecido
    usuario = Funcionarios.objects.filter(Nome=nome).first()

    # Se o usuário existe, autentica usando o método authenticate
    if usuario:
        if usuario and usuario.Senha == senha:
            print('autenticou!!!!')
            produtos = Produtos.objects.all()
            return render(request, 'produto.html', {'produtos': produtos})
        else:
            # Exibindo a mensagem de usuario ou senha incorreto (no caso apenas a senha esta incorreta)
            messages.success(request, 'Usuario ou senha incorretos')
            return redirect('login')
    else:
        # Exibindo a mensagem de usuario nao encontrado
        messages.success(request, 'Nao existe nenhum usuario com esse nome')
        return redirect('login')