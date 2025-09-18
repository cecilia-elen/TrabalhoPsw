from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages #para essa parte de avisos de sucesso ou erro e tals
from django.contrib.auth.decorators import login_required, permission_required
from usuario.models import Usuario
from django.contrib.auth import get_user_model
from .forms import UsuarioForm, UsuarioUpdateForm, LoginForm, AdminUsuarioUpdateForm

def cadastro(request):
    if request.method == 'POST':
        # Usamos o novo formulário de criação, mais curto
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            # Redireciona o novo usuário para completar o perfil!
            return redirect(reverse('usuario:perfil'))
    else:
        form = UsuarioForm()

    context = {'form': form}
    return render(request, 'usuario/cadastro.html', context)






@login_required
def editar_perfil(request):
    perfil_do_usuario = request.user.usuario

    if request.method == 'POST':
        # Lembrar do request.FILES para a foto
        form = UsuarioUpdateForm(request.POST, request.FILES, instance=perfil_do_usuario)
        if form.is_valid():
            form.save()
            # Redireciona para a página de perfil para ver as alterações
            messages.success(request, 'Seu perfil foi atualizado com sucesso!')
            return redirect(reverse('usuario:perfil'))

        else:
            messages.error(request, 'Houve um erro. Por favor, verifique os campos.')
            form = UsuarioUpdateForm(instance=request.user)
    else:
        form = UsuarioUpdateForm(instance=perfil_do_usuario)

    contexto = {'form': form}
    return render(request, 'usuario/editar_perfil.html', contexto)






def login_user(request):
     # Se o usuário já está logado, redireciona para a página inicial
    if request.user.is_authenticated:
        return redirect(reverse('pagina-inicial'))
        
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(reverse('pagina-inicial'))
    else:
         # Cria um formulário de login em branco
        form = LoginForm()
 # Envia o formulário (em branco ou com erros) para o template
    context = {'form': form}

    return render(request, 'usuario/login.html', context)


def logout_user(request):
    logout(request)

    return redirect(reverse('pagina-inicial'))
 #Desloga o usuário e o redireciona para a página inicial.


@login_required
def perfil(request, pk=None):
    #Renderiza a página de perfil. Se um 'pk' (ID do usuário) for fornecido na URL, mostra o perfil desse usuário, senao, mostra o perfil da pessoa logada
    User = get_user_model() # Pega o modelo User padrão
    
    if pk:
        # Estamos tentando ver o perfil de outra pessoa
        usuario_alvo = get_object_or_404(User, pk=pk)
    else:
        # Estamos vendo nosso próprio perfil
        usuario_alvo = request.user
    
    contexto = {
        # Enviamos para o template quem é o "dono" do perfil que estamos vendo
        'usuario_alvo': usuario_alvo
    }
    
    # Vamos usar um template chamado 'perfil.html' para exibir as informações
    return render(request, 'usuario/perfil.html', contexto)





@login_required
def excluir_usuario(request):
    # Verifica se o formulário de confirmação foi enviado)
    if request.method == 'POST':
        usuario = request.user
        # fazer o logout antes de deletar, para limpar a sessão
        logout(request) 
        #  deleta o usuário do banco de dados
        usuario.delete()
        messages.success(request, 'Conta foi excluída com sucesso.')
        return redirect('pagina-inicial')
#Página de confirmação de exclusao para previnir decisões arriscadas
    return render(request, 'usuario/excluir_confirmacao.html')





@login_required
def visualizar_usuario(request):
    #Renderiza a página com todos os detalhes do perfil do usuário logado.
    return render(request, 'usuario/visualizar_usuario.html')






@login_required
@permission_required('usuario.view_usuario', raise_exception=True)
def listar_usuarios(request):
    # Buscamos os objetos Usuario
    usuarios = Usuario.objects.all().order_by('first_name')
    return render(request, 'usuario/listar_usuarios.html', {'usuarios': usuarios})




@login_required
@permission_required('usuario.delete_usuario', raise_exception=True)
def excluir_usuario_admin(request, pk):
    #View para um admin excluir qualquer usuário do sistema, com página de confirmação.
    # Busca-se o usuário alvo da exclusão.
    usuario_alvo = get_object_or_404(Usuario, pk=pk)

    # Se receber uma requisição, apaga (vinda do botão de confirmação)
    if request.method == 'POST':
        # Impede que o admin se auto-exclua pelo painel de gerenciamento.
        if request.user == usuario_alvo:
            messages.error(request, "Você não pode excluir sua própria conta de administrador a partir daqui.")
            return redirect('usuario:listar_usuarios')
        nome_alvo = usuario_alvo.get_full_name() or usuario_alvo.username # Guarda o nome para a mensagem de sucesso
        usuario_alvo.delete()
        messages.success(request, f'O usuário "{nome_alvo}" foi excluído com sucesso.')
        return redirect('usuario:listar_usuarios')

    # Prepara o contexto para a página de confirmação
    contexto = {'item_a_excluir': usuario_alvo, 'tipo': 'Usuário'}
    return render(request, 'usuario/excluir_confirmacao.html', contexto)



@login_required
@permission_required('usuario.change_usuario', raise_exception=True)
def alterar_usuario_admin(request, pk):
    #View para um admin editar as informações de qualquer usuário do sistema.
    # Busca o usuário que será editado pelo seu ID (pk). Se não encontrar, retorna erro 404.
    usuario_alvo = get_object_or_404(Usuario, pk=pk)

    if request.method == 'POST':
        # Cria o formulário preenchido com os dados enviados e os arquivos
        form = AdminUsuarioUpdateForm(request.POST, request.FILES, instance=usuario_alvo)
        if form.is_valid():
            # Prepara o objeto usuario com os dados do form, mas não salva no banco ainda
            form.save()
            
            messages.success(request, f'Os dados do usuário "{usuario_alvo.username}" foram atualizados com sucesso.')
            return redirect('usuario:listar_usuarios')
    else:
        # Usa o formulário AdminUsuarioUpdateForm para exibir os dados.
        form = AdminUsuarioUpdateForm(instance=usuario_alvo)

    #Cria o contexto para enviar as variáveis para o template.
    contexto = {
        'form': form,
        'usuario_alvo': usuario_alvo
    }

    return render(request, 'usuario/alterar_usuario_admin.html', contexto)



@login_required
@permission_required('usuario.add_usuario', raise_exception=True)
def criar_usuario_admin(request):
    #View para um admin CRIAR um novo usuário
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            novo_usuario = form.save()
            messages.success(request, f'O usuário "{novo_usuario.username}" foi criado com sucesso!')
            return redirect('usuario:listar_usuarios')
    else:
        form = UsuarioForm()

    return render(request, 'usuario/criar_usuario_admin.html', {'form': form})
