from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UsuarioForm, LoginForm
from .forms import UsuarioForm, UsuarioUpdateForm, LoginForm

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
    if request.method == 'POST':
        # Lembrar do request.FILES para a foto
        form = UsuarioUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            # Redireciona para a página de perfil para ver as alterações
            return redirect(reverse('usuario:perfil'))

    else:
        # Preenche o formulário com os dados atuais do usuário
        form = UsuarioUpdateForm(instance=request.user)

    context = {'form': form}
    # Precisamos de um novo template para esta página
    return render(request, 'usuario/editar_perfil.html', context)

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
def perfil(request):
    """Renderiza a página de perfil do usuário logado."""
    # Rodar o Perfil do usuário com suas informações basiconas
    return render(request, 'usuario/perfil.html')

@login_required
def excluir_usuario(request):
    usuario = request.user
    usuario.delete()
    return redirect('pagina-inicial')

@login_required
def visualizar_usuario(request):
    #Renderiza a página com todos os detalhes do perfil do usuário logado.
    return render(request, 'usuario/visualizar_usuario.html')