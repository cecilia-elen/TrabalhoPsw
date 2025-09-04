from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
    # Rota principal para listar e criar produtos
    path('', views.gerenciar_produtos, name='gerenciar_produtos'),
    #pega o id do produto pra alterar ele
    path('<int:pk>/alterar/', views.alterar_produto, name='alterar_produto'),
    #pega o id do produto para excluir ele 
    path('excluir/<int:pk>', views.excluir_produto, name='excluir_produto'),
    #Pro adm poder visualizar todos os produtos e apagar aqueles que violam as condutas morais. Não faz sentido ele criar e editar catálogos de outras pessoas pq isso violaria a autoria dos catálogos
    path('ADM/', views.listar_produtos, name='listar_produtos'),
    path('ADM/<int:pk>', views.excluir_produto_admin, name='excluir_produto_confirmar'),
]
