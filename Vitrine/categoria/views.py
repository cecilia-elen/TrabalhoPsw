from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Categoria
from .forms import CategoriaForm
from django.urls import reverse
from django.contrib import messages #Negócio para colocar mensagens

@login_required 
def gerenciar_categorias(request):
     #Lógica para criar uma nova categoria (quando o formulário é enviado)
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
#mensagem de sucesso
            messages.success(request, 'Categoria criada com sucesso!')
             #Redireciona para a mesma página para limpar o formulário e ver a nova categoria na lista
            return redirect('categoria:gerenciar_categorias') 
    else:
         #Se não for POST, apenas cria um formulário em branco
        form = CategoriaForm()

     #Busca todas as categorias existentes para listar na página
    categorias_existentes = Categoria.objects.all().order_by('categoria_pai__nome', 'nome')
    #organiza todas as categorias existentes em um forms
    context = {'form': form,'categorias': categorias_existentes}
    
    return render(request, 'categoria/gerenciar_categorias.html', context)

@login_required
def alterar_categoria(request, pk):
    # Busca a categoria específica pelo seu ID (pk) ou retorna erro 404
    categoria = get_object_or_404(Categoria, pk=pk)
    
    if request.method == 'POST':
        # Preenche o formulário com os dados enviados E com a instância da categoria que estamos editando
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria alterada com sucesso!')
            return redirect('categoria:gerenciar_categorias')
    else:
        # Cria o formulário já preenchido com os dados da categoria existente
        form = CategoriaForm(instance=categoria)

    context = {
        'form': form,
        'categoria': categoria
    }
    return render(request, 'categoria/alterar_categoria.html', context)

@login_required
def excluir_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    
    if request.method == 'POST':
        # Se o formulário de confirmação for enviado, exclui o objeto
        categoria.delete()
        messages.success(request, 'Categoria excluída com sucesso!')
        return redirect('categoria:gerenciar_categorias')

    context = {
        'categoria': categoria
    }
    return render(request, 'categoria/excluir_categoria_confirmar.html', context)