from django.urls import path
from . import views

app_name = 'catalogo'

urlpatterns = [
    path('criar/', views.criar_catalogo, name='criar_catalogo'),
    #pega o id do catálogo e faz o print dele em pdf
    #path('<int:catalogo_id>/download/', views.gerar_pdf_catalogo, name='download_catalogo'),
]