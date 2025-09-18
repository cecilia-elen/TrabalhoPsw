from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CatalogoForm
from django.urls import reverse

@login_required
def criar_catalogo(request):
    if request.method == 'POST':
        # request.FILES para lidar com o upload da thumbnail
        form = CatalogoForm(request.POST, request.FILES)
        if form.is_valid():
            catalogo = form.save(commit=False)
            catalogo.dono = request.user
            catalogo.save()
            
            # Redireciona para a página de detalhes do catálogo para colocar seus itens, o "pk" é para que sua chave de identificação seja coletada, já que o usuário pode ter mais que um catálogo e ele precisa ser diferenciado
            return redirect(reverse('catalogo:detalhe_catalogo', kwargs={'pk': catalogo.pk}))
    else:
        form = CatalogoForm()
    
    return render(request, 'catalogo/criar_catalogo.html', {'form': form})

@login_required
def detalhe_catalogo(request, pk):
    """
    Mostra os detalhes de um catálogo específico.
    """
    catalogo = get_object_or_404(Catalogo, pk=pk, dono=request.user)
    context = {
        'catalogo': catalogo
    }
    return render(request, 'catalogo/detalhe_catalogo.html', context)

#def gerar_pdf_catalogo(request, catalogo_id):
