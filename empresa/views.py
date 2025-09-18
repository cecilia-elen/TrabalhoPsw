from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .forms import EmpresaForm
from .models import Empresa
from catalogo.models import Catalogo 

@login_required
def gerenciar_empresa(request):
    #Lista todas as empresas cadastradas pelo usuário logado
    empresas = Empresa.objects.filter(responsavel=request.user)
    return render(request, 'empresa/gerenciar_empresa.html', {'empresas': empresas})

@login_required
def adicionar_empresa(request):
    #View para o formulário de CRIAÇÃO de uma nova empresa
    if request.method == 'POST':
        form = EmpresaForm(request.POST, request.FILES)
        if form.is_valid():
            nova_empresa = form.save(commit=False)
            nova_empresa.responsavel = request.user
            nova_empresa.save()
            messages.success(request, 'Nova empresa criada com sucesso!')
            return redirect('empresa:gerenciar_empresa')
    else:
        #porque se a pessoa não preencher, o endereço vai ser o que ela colocou no perfil
        dados_iniciais = {
            'estado': request.user.usuario.estado, 'cidade': request.user.usuario.cidade,
            'bairro': request.user.usuario.bairro, 'logradouro': request.user.usuario.logradouro,
            'numero': request.user.usuario.numero, 'detalhamento': request.user.usuario.detalhamento,
        }
        form = EmpresaForm(initial=dados_iniciais)
        
    return render(request, 'empresa/adicionar_empresa.html', {'form': form})

@login_required
def alterar_empresa(request, pk):
    #View para o formulário de EDIÇÃO de uma empresa existente
    empresa = get_object_or_404(Empresa, pk=pk, responsavel=request.user)
    if request.method == 'POST':
        form = EmpresaForm(request.POST, request.FILES, instance=empresa)
        if form.is_valid():
            form.save()
            messages.success(request, f'Os dados da empresa "{empresa.nome}" foram atualizados!')
            return redirect('empresa:gerenciar_empresa')
    else:
        form = EmpresaForm(instance=empresa)
        
    contexto = {'form': form, 'empresa': empresa}
    return render(request, 'empresa/alterar_empresa.html', contexto)

@login_required
def excluir_empresa(request, pk):
    #Lida com a confirmação e exclusão de uma empresa
    empresa = get_object_or_404(Empresa, pk=pk, responsavel=request.user)
    
    # Se o formulário de confirmação foi enviado (método POST)
    if request.method == 'POST':
        nome_empresa = empresa.nome
        empresa.delete()
        messages.success(request, f'A empresa "{nome_empresa}" foi excluída com sucesso!')
        return redirect('empresa:gerenciar_empresa')
    
    # Se for um clique normal no link (método GET), mostra a página de confirmação
    contexto = {'empresa': empresa}
    return render(request, 'empresa/excluir_empresa.html', contexto)
#mostra o perfil de uma empresa em específico, seja do usuário ou de qualquer outra pessoa 
@login_required
def perfil_empresa(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    catalogos = Catalogo.objects.filter(empresa=empresa)
    usuario_alvo = empresa.responsavel
    contexto = {'empresa': empresa, 'catalogos': catalogos, 'usuario_alvo': usuario_alvo}
    return render(request, 'empresa/perfil_empresa.html', contexto)


@login_required
@permission_required('empresa.view_empresa', raise_exception=True)
def listar_empresas(request):
    empresas = Empresa.objects.all().order_by('nome')
    return render(request, 'empresa/listar_empresas.html', {'empresas': empresas})

@login_required
@permission_required('empresa.delete_empresa', raise_exception=True)
def excluir_empresa_admin(request, pk):
    # Busca a empresa do sistema pelo seu ID
    empresa = get_object_or_404(Empresa, pk=pk)
    
    if request.method == 'POST':
        nome_empresa = empresa.nome
        empresa.delete()
        messages.success(request, f'A empresa "{nome_empresa}" foi excluída com sucesso.')
        return redirect('empresa:listar_empresas') # Volta para a lista de empresas do admin
    
    # Prepara o contexto para o template genérico de confirmação
    contexto = {
        'empresa': empresa,
        'tipo': 'Empresa'
    }
    return render(request, 'empresa/excluir_empresa.html', contexto)
#