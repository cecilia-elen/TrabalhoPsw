from django.urls import path
from . import views

app_name = 'usuario'

urlpatterns = [
    # Quando a URL for /usuario/cadastro/, esta view será chamada
    path('cadastro/', views.cadastro, name="cadastro"),
    # Quando a URL for /usuario/login/, esta view será chamada
   path('login/', views.login_user, name="login"),
     # Quando a URL for /usuario/logout/, esta view será chamada
   path('logout/', views.logout_user, name="logout"),
   #URL pra ver o próprio perfil 
   path('perfil/', views.perfil, name='perfil'),
   # URL para ver o perfil de OUTRA PESSOA (ex: /usuario/perfil/5/)
    path('perfil/<int:pk>/', views.perfil, name='perfil_publico'),
   # Quando o usuário quiser excluir a conta, esta view será chamada
  path('excluir/', views.excluir_usuario, name='excluir_confirmacao'),
# Quando o usuário quiser ver seus dados, esta view será chamada
 path('perfil/detalhes/', views.visualizar_usuario, name="visualizar_usuario"),
  # Quando o usuário quiser editar a conta, esta view será chamada
  path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
  #listagem de usuários pro adm poder editar, excluir, visualizar e criar
  path('ADM/usuarios', views.listar_usuarios, name='listar_usuarios'),
  path('ADM/usuarios/criar/', views.criar_usuario_admin, name='criar_usuario_admin'),
  path('ADM/usuarios/alterar/<int:pk>/', views.alterar_usuario_admin, name='alterar_usuario_admin'),
  path('ADM/excluir/<int:pk>/', views.excluir_usuario_admin, name='excluir_usuario_admin'),

]
#