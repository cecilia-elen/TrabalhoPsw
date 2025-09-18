from django.urls import path
from . import views

app_name = 'empresa'

urlpatterns = [
    #Link para excluir, alterar e visualizar as empresas que a pessoa tem
    path('gerenciar/', views.gerenciar_empresa, name='gerenciar_empresa'),
# Uma única URL para criar
    path('adicionar/', views.adicionar_empresa, name='adicionar_empresa'),
#O ADM pode ver e excluir empresas (pq n faz sentido ele alterar e criar a empresa dos outros...)
    path('ADM/', views.listar_empresas, name='listar_empresas'),
   path('ADM/excluir/<int:pk>/', views.excluir_empresa_admin, name='excluir_empresa_admin'),
        # URL para a ação de excluir. Precisam do (pk) da empresa
    path('excluir/<int:pk>/', views.excluir_empresa, name='excluir_empresa'),
#para mostrar o perfil da empresa
     path('perfil/<int:pk>/', views.perfil_empresa, name='perfil_empresa'),
     #pra alterar a empresa em específico 
      path('alterar/<int:pk>/', views.alterar_empresa, name='alterar_empresa'),
]