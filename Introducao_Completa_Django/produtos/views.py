from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Produto

# Create your views here.
def cadastrar(request):
    if request.method == "GET":
        cd_erro = request.GET.get('cd_erro')
        texto = request.GET.get('texto')
        print(cd_erro)
        return render(request, 'cadastrar.html',{'cd_erro': cd_erro, 'texto': texto})
    elif request.method == "POST":
        produto = request.POST.get('produto') #RECEBENDO OS PARÂMETROS DO FORMULÁRIO
        preco = request.POST.get('preco')

        if len(produto) <= 0:
            return redirect('/produtos/cadastrar/?cd_erro=1&texto=DIGITE O NOME DO PRODUTO')

        produto = Produto(
            nome_produto=produto,
            preco=preco
        )

        produto.save()

        return redirect('/produtos/listar')

def listar(request):
    #filtrando os itens do formulário
    nome_filtrar = request.GET.get('nome_filtrar')
    if nome_filtrar:
        produtos = Produto.objects.filter(nome_produto__icontains=nome_filtrar)
    else:
          #buscando os dados que estão no banco de dados
        produtos = Produto.objects.all()
  

    return render(request, 'listar.html',{'produtos': produtos})


def deletar(request, id):
    produto = Produto.objects.get(id=id)
    produto.delete()
    return redirect('/produtos/listar')