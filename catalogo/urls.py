from django.urls import path
from . import views

app_name = 'catalogo'

urlpatterns = [
    #criação de catálogo
    path('criar/', views.criar_catalogo, name='criar_catalogo'),
    #alteração de catálogo
    path('alterar/<int:pk>/', views.alterar_catalogo, name='alterar_catalogo'),
    #do usuário ver o catálogo dele
    path('meus-catalogos/', views.visualizar_catalogos, name='visualizar_catalogos'),
    #tira o produto do catalogo
    path('remover-produto/<int:cp_pk>/', views.remover_produto_catalogo, name='remover_produto_catalogo'),
    #remover o catalgo na visao do usuario
    path('excluir/<int:pk>/', views.excluir_catalogo, name='excluir_catalogo'),

     #pega o id do catálogo e faz o print dele em pdf
    #path('<int:catalogo_id>/download/', views.gerar_pdf_catalogo, name='download_catalogo'),
    #mostra o catálago com seus produtos
    path('detalhe/<int:pk>/', views.detalhe_catalogo, name='detalhe_catalogo'),
    #adiciona produtos existentes em um catálogo através de catalogo_produto
    path('<int:catalogo_pk>/adicionar-produto/', views.adicionar_produto_catalogo, name='adicionar_produto_catalogo'),
    #Pro adm poder visualizar todos os catalogos e apagar aqueles que violam as condutas morais. Não faz sentido ele criar e editar catálogos de outras pessoas pq isso violaria a autoria dos catálogos
    path('ADM/', views.listar_catalogos, name='listar_catalogos'),
    #pro adm excluir se ele ver necessidade
    path('excluir/<int:pk>/', views.excluir_catalogo_admin, name='excluir_catalogo'),
    

]