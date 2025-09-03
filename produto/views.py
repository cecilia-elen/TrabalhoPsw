from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages #import que avisa se deu certo adicionar o produto, alterar
from .forms import ProdutoForm
from .models import Produto

# em produto/views.py (nenhuma mudança necessária aqui)

@login_required
def gerenciar_produtos(request):
    #Verifica se o usuário tem pelo menos uma empresa
    if not request.user.empresas.exists():
        messages.error(request, 'Você precisa cadastrar uma empresa antes de gerenciar produtos.')
        return redirect('empresa:gerenciar_empresa')
    
        # Vai pegar o usuário para salvar o produto no nome da empresa dele no dropdown
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto adicionado com sucesso!')
            return redirect('produto:gerenciar_produtos') 
    else:
        # Também passa no GET para preencher o dropdown corretamente.
        form = ProdutoForm(user=request.user)
        produtos_do_usuario = Produto.objects.filter(empresa__usuario=request.user).order_by('-id')

        contexto = {
        'form': form,
        'produtos': produtos_do_usuario
    }

        return render(request, 'produto/gerenciar_produtos.html', contexto)

@login_required
def alterar_produto(request, pk):
      # Busca o produto e garante que ele pertence a uma das empresas do usuário
    produto = get_object_or_404(Produto, pk=pk, empresa__usuario=request.user)
    
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES, instance=produto, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto alterado com sucesso!') #mensagemzinha que sinaliza se deu certo
            return redirect('produto:gerenciar_produtos')
    else:
        # Preenche o formulário com os dados do produto que estamos editando
        form = ProdutoForm(instance=produto, user=request.user)

    context = {
        'form': form,
        'produto': produto
    }
    return render(request, 'produto/alterar_produto.html', context)

@login_required
def excluir_produto(request, pk):
    # Busca o produto, garantindo que pertence ao usuário logado (de novo)
    produto = get_object_or_404(Produto, pk=pk, empresa__usuario=request.user)
    
    if request.method == 'POST':
        produto.delete()
        messages.success(request, 'Produto excluído com sucesso!') #mensagemzinha que sinaliza se deu certo
        return redirect('produto:gerenciar_produtos') #Volta para a parte de criar/ver produtos

    context = {
        'produto': produto
    }
    return render(request, 'produto/excluir_produto_confirmar.html', context)

@login_required
@permission_required('produto.view_produto', raise_exception=True)
def listar_produtos(request):
    produtos = Produto.objects.all().order_by('nome')
    return render(request, 'produto/listar_produtos.html', {'produtos': produtos})

@login_required
@permission_required('produto.delete_produto', raise_exception=True)
def excluir_produto_admin(request, pk):
    # Busca o produto do sistema pelo seu ID
    produto = get_object_or_404(Produto, pk=pk)

    if request.method == 'POST':
        nome_produto = produto.nome
        produto.delete()
        messages.success(request, f'O produto "{nome_produto}" foi excluído com sucesso.')
        return redirect('produto:listar_produtos') # Volta para a lista de produtos do admin
        
    contexto = {
        'item': produto,
        'tipo': 'Produto'
    }
    return render(request, 'produto/excluir_produto_confirmar.html', contexto)