from django.urls import path
from . import views

app_name = 'categoria'

urlpatterns = [
    path('ADM/', views.gerenciar_categorias, name='gerenciar_categorias'),
    #pega o id da categoria para alterar ela 
    path('<int:pk>/alterar/', views.alterar_categoria, name='alterar_categoria'),
    #pega o id para excluir a categoria
    path('<int:pk>/excluir/', views.excluir_categoria, name='excluir_categoria'),

]