from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages #import que avisa se deu certo adicionar o produto, alterar
from .forms import ProdutoForm
from .models import Produto

@login_required
def gerenciar_produtos(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            produto = form.save(commit=False)
            
            # Define o criador do produto como o usuário logado
            produto.usuario = request.user
            
            # Se o usuário tiver uma empresa, associa o produto a ela também
            if hasattr(request.usuari, 'empresa') and request.usuario.empresa:
                produto.empresa = request.user.empresa

            produto.save()
            messages.success(request, 'Produto criado com sucesso!')
            return redirect('produto:gerenciar_produtos')
    else:
        form = ProdutoForm()

    # Filtra a lista para mostrar apenas produtos criados pelo usuário logado
    produtos_do_usuario = Produto.objects.filter(usuario=request.user)
    
    context = {
        'form': form,
        'produtos': produtos_do_usuario
    }
    return render(request, 'produto/gerenciar_produtos.html', context)