<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 60e0c3e232c3b9522bac92c41a6682a34c1e7220
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .forms import CatalogoForm
from .forms import Catalogo
from .forms import CatalogoForm
from produto.models import Catalogo, Catalogo_Produto
from produto.forms import Catalogo_ProdutoForm 
from django.urls import reverse


@login_required
def criar_catalogo(request):
    # Verifica se o usuário tem PELO MENOS UMA empresa cadastrada
    if not request.user.empresas.exists():
        messages.error(request, 'Você precisa cadastrar uma empresa antes de criar um catálogo.')
        return redirect('empresa:gerenciar_empresa')
    
    if request.method == 'POST':
        # Passamos para o formulário no POST.
        form = CatalogoForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            catalogo = form.save()
            messages.success(request, f'Catálogo "{catalogo.título}" criado com sucesso! Agora adicione produtos a ele.')
            return redirect(reverse('catalogo:detalhe_catalogo', kwargs={'pk': catalogo.pk}))
    else:
        form = CatalogoForm(user=request.user)
    
    return render(request, 'catalogo/criar_catalogo.html', {'form': form})



def detalhe_catalogo(request, pk):
    # Pega o catálogo específico ou mostra um erro 404
    catalogo = get_object_or_404(Catalogo, pk=pk)
    # Pega todos os produtos que pertencem a este catálogo
    catalogo_produtos = Catalogo_Produto.objects.filter(catalogo=catalogo)
    # Verifica se o usuário logado é o dono do catálogo
    is_owner = False
    if request.user.is_authenticated:
        if request.user == catalogo.empresa.usuario:
            is_owner = True

    context = {
        'catalogo': catalogo,
        'catalogo_produtos': catalogo_produtos,
        'is_owner': is_owner
    }
    return render(request, 'catalogo/detalhe_catalogo.html', context)

#def gerar_pdf_catalogo(request, catalogo_id):


@login_required
def listar_catalogos(request):
    catalogos = Catalogo.objects.all().order_by('empresa__usuario__first_name', 'título')
    return render(request, 'catalogo/listar_catalogos.html', {'catalogos': catalogos})


def excluir_catalogo_admin(request, pk):
    # Busca o catálogo pelo ID ou retorna um erro 404 se não encontrar
    catalogo = get_object_or_404(Catalogo, pk=pk)
    # Guarda o nome para usar na mensagem antes de deletar
    nome_catalogo = catalogo.título
    catalogo.delete()
    # mensagem de sucesso
    messages.success(request, f'O catálogo "{nome_catalogo}" foi excluído com sucesso.')
    # Redireciona o admin de volta para a página de listagem
    return redirect('catalogo:listar_catalogos')

@login_required
def visualizar_catalogos(request):
    # Filtra os catálogos para pegar apenas aqueles cuja empresa pertence ao usuário logado
    catalogos = Catalogo.objects.filter(empresa__usuario=request.user).order_by('-id')
    context = {
        'catalogos': catalogos
    }
    return render(request, 'catalogo/visualizar_catalogos.html', context)


    # catalogo/views.py
from .forms import CatalogoForm # Garanta que seu form está importado

# ... (suas outras views)

@login_required
def alterar_catalogo(request, pk):
    # Pega o catálogo que será editado
    catalogo = get_object_or_404(Catalogo, pk=pk)

    if request.method == 'POST':
        # Preenche o formulário com os dados enviados E com a instância do catálogo
        form = CatalogoForm(request.POST, request.FILES, instance=catalogo, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Catálogo "{catalogo.título}" alterado com sucesso!')
            return redirect('catalogo:visualizar_catalogos')
    else:
        # Abre o formulário preenchido com os dados atuais do catálogo
        form = CatalogoForm(instance=catalogo, user=request.user)
    
    context = {
        'form': form,
        'catalogo': catalogo
    }
    return render(request, 'catalogo/alterar_catalogo.html', context)


@login_required
def adicionar_produto_catalogo(request, catalogo_pk):
    # Pega o catálogo que a pesoa adicionar o produto
    catalogo = get_object_or_404(Catalogo, pk=catalogo_pk)

    if request.method == 'POST':
        # Instancia o form com os dados enviados e com a empresa do catálogo para filtrar os produtos que ela tem
        form = Catalogo_ProdutoForm(catalogo.empresa, request.POST)
        if form.is_valid():
            # Verifica se o produto já não está no catálogo para evitar erros
            produto_selecionado = form.cleaned_data['produto']
            if Catalogo_Produto.objects.filter(catalogo=catalogo, produto=produto_selecionado).exists():
                messages.warning(request, f'O produto "{produto_selecionado.nome}" já está neste catálogo.')
            else:
                # Salva na memória, sem enviar ao banco ainda
                catalogo_produto = form.save(commit=False)
                # Coloca no catalogo se já n tiver nele 
                catalogo_produto.catalogo = catalogo
                # Agora sim, salva no banco de dados
                catalogo_produto.save()
                messages.success(request, f'Produto "{catalogo_produto.produto.nome}" adicionado ao catálogo com sucesso!')
            
            return redirect('catalogo:detalhe_catalogo', pk=catalogo.pk)
    
    # Se for o primeiro acesso à página (método GET)
    else:
        # Essa linha tá pegando a empresa que foi mandada pelo catálogo e mandando lá pro forms filtrar só os produtos dela
        form = Catalogo_ProdutoForm(empresa=catalogo.empresa)

    context = {
        'form': form,
        'catalogo': catalogo
    }
    return render(request, 'catalogo/adicionar_produto_catalogo.html', context)

@login_required
def remover_produto_catalogo(request, cp_pk):
    # Encontra a ligação específica entre o catálogo e o produto
    item_a_remover = get_object_or_404(Catalogo_Produto, pk=cp_pk)


    # Guarda o ID do catálogo para podermos voltar para a página certa
    catalogo_id = item_a_remover.catalogo.pk
    nome_produto = item_a_remover.produto.nome

    # Apaga APENAS a ligação. O produto original continua intacto.
    item_a_remover.delete()

    messages.success(request, f'O produto "{nome_produto}" foi removido do catálogo com sucesso.')
    
    # Redireciona o usuário de volta para a página de detalhes do catálogo
    return redirect('catalogo:detalhe_catalogo', pk=catalogo_id)


@login_required
def excluir_catalogo(request, pk):
    # Pega o catálogo que queremos excluir
    catalogo = get_object_or_404(Catalogo, pk=pk)

    # Se o formulário de confirmação foi enviado (POST)
    if request.method == 'POST':
        nome_catalogo = catalogo.título
        catalogo.delete()
        messages.success(request, f'O catálogo "{nome_catalogo}" foi excluído com sucesso!')
        
        # Se for admin, volta para a lista de admin. Senão, volta para a lista do usuário.
        if request.user.is_staff:
            return redirect('catalogo:listar_catalogos')
        else:
            return redirect('catalogo:visualizar_catalogos')
    
    # No o primeiro acesso (GET), apenas mostra a página de confirmação
    contexto = {'catalogo': catalogo}
<<<<<<< HEAD
    return render(request, 'catalogo/excluir_catalogo.html', contexto)
=======
    return render(request, 'catalogo/excluir_catalogo.html', contexto)
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> 1cea6da5e9c6ae1a5fcfbe83fecbbd074ab1453d
>>>>>>> 60e0c3e232c3b9522bac92c41a6682a34c1e7220
