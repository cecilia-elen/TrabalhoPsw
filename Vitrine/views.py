<<<<<<< HEAD
from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.models import User
from empresa.models import Empresa
from catalogo.models import Catalogo
from django.contrib.auth.decorators import login_required


def pagina_inicial(request):
    # Esta função simplesmente diz ao Django para encontrar e mostrar o arquivo 'index.html'
    # Ele vai procurar na pasta templates que configuramos no settings.py e vai ser a primeira página a rodar quando a gente entra no sistema
    return render(request, 'index.html')


#só quem tiver logado pode pesquisar coisas no site 
@login_required
def resultados_busca(request):
    # Pega o termo de busca da URL (ex: /buscar/?q=meu-termo)
    query = request.GET.get('q', '')
    
    resultados_usuario = []
    resultados_empresa = []
    resultados_catalogo = []

    if query:
        # Busca por Usuários (no username, nome ou sobrenome), a busca é no User, mas o resultado será o perfil completo
        resultados_usuario = User.objects.filter(
            Q(username__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query)
        )

        # Busca por Empresas (no nome ou ramo)
        resultados_empresa = Empresa.objects.filter(
            Q(nome__icontains=query) |
            Q(ramo__icontains=query)
        )

        # Busca por Catálogos
        # - no nome, descrição ou categoria do catálogo
        # - OU no nome ou categoria dos produtos DENTRO do catálogo
        resultados_catalogo = Catalogo.objects.filter(
            Q(nome__icontains=query) |
            Q(descricao__icontains=query) |
            Q(categoria__nome__icontains=query) |
            Q(produtos__nome__icontains=query) |
            Q(produtos__categoria__nome__icontains=query)
        ).distinct() # .distinct() para não mostrar o mesmo catálogo várias vezes

    contexto = {
        'query': query,
        'usuarios': resultados_usuario,
        'empresas': resultados_empresa,
        'catalogos': resultados_catalogo,
    }
    
    # O Django vai procurar este template em uma pasta 'templates' na raiz do projeto,
    return render(request, 'vitrine/resultados_busca.html', contexto)
#
=======
# Dentro do arquivo Vitrine/views.py

from django.shortcuts import render

def pagina_inicial(request):
    # Esta função simplesmente diz ao Django para encontrar e mostrar o arquivo 'index.html'
<<<<<<< HEAD
    # Ele vai procurar na pasta templates que configuramos no settings.py e vai ser a primeira página a rodar quando a gente entra no sistema
=======
<<<<<<< HEAD
    # Ele vai procurar na pasta templates que configuramos no settings.py e vai ser a primeira página a rodar quando a gente entra no sistema
=======
    # Ele vai procurar na pasta templates que configuramos no settings.py
>>>>>>> 1cea6da5e9c6ae1a5fcfbe83fecbbd074ab1453d
>>>>>>> 60e0c3e232c3b9522bac92c41a6682a34c1e7220
    return render(request, 'index.html')
>>>>>>> 8750437900de8beadd7384be3adc93d797d65d08
