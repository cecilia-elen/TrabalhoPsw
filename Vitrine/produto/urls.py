from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
    # Rota principal para listar e criar produtos
    path('', views.gerenciar_produtos, name='gerenciar_produtos'),
    #pega o id do produto pra alterar ele (isso aqui vc descomenta depois)
    #path('<int:pk>/alterar/', views.alterar_produto, name='alterar_produto'),
    #pega o id do produto para excluir ele 
    #path('<int:pk>/excluir/', views.excluir_produto, name='excluir_produto'),
]