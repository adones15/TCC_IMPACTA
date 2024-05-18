from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from .models import Produtos, Funcionarios, EntradaProdutos
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render
from django.db import connection

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

def entrada(request):
    # POST
    if request.method == 'POST':
        id = request.POST.get('id')
        nfiscal = request.POST.get('nfiscal')
        Data_Entrada = request.POST.get('Data_Entrada')
        quantidade = request.POST.get('quantidade')
        preco = request.POST.get('preco')
        fornecedor = request.POST.get('fornecedor')

        # Criar uma nova instância do modelo da entrada com os dados do formulário
        entrada_produtos = EntradaProdutos(ID_Produto=id, Numero_Nota_Fiscal=nfiscal, Data_Entrada=Data_Entrada, Quantidade_Entrada=quantidade, Preco_Unitario=preco, Fornecedor=fornecedor)
                
        # Salvar o novo produto no banco de dados
        entrada_produtos.save()

        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT ep.ID_Entrada,
            ep.ID_Produto,
            p.Nome,
            ep.Numero_Nota_Fiscal,
            ep.Data_Entrada,
            ep.Quantidade_Entrada,
            ep.Preco_Unitario,
            (ep.Quantidade_Entrada * ep.Preco_Unitario) as Preco_Total,
            ep.Fornecedor
            FROM entrada_produtos ep
            JOIN produtos p ON p.ID_Produto = ep.ID_Produto;
            """)
            rows = cursor.fetchall()

            # Processando os resultados
            column_names = [col[0] for col in cursor.description]
            entradas = [
                dict(zip(column_names, row))
                for row in rows
            ]

        produtos = Produtos.objects.all()
        return render(request, './entrada.html', {'produtos': produtos, 'entradas': entradas})
    else:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT ep.ID_Entrada,
                ep.ID_Produto,
                p.Nome,
                ep.Numero_Nota_Fiscal,
                ep.Data_Entrada,
                ep.Quantidade_Entrada,
                ep.Preco_Unitario,
                (ep.Quantidade_Entrada * ep.Preco_Unitario) as Preco_Total,
                ep.Fornecedor
                FROM entrada_produtos ep
                JOIN produtos p ON p.ID_Produto = ep.ID_Produto;
            """)
            rows = cursor.fetchall()

            # Processando os resultados
            column_names = [col[0] for col in cursor.description]
            entradas = [
                dict(zip(column_names, row))
                for row in rows
            ]

        produtos = Produtos.objects.all()
        return render(request, './entrada.html', {'produtos': produtos, 'entradas': entradas})
