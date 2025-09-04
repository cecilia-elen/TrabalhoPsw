# Dentro do arquivo Vitrine/views.py

from django.shortcuts import render

def pagina_inicial(request):
    # Esta função simplesmente diz ao Django para encontrar e mostrar o arquivo 'index.html'
<<<<<<< HEAD
    # Ele vai procurar na pasta templates que configuramos no settings.py e vai ser a primeira página a rodar quando a gente entra no sistema
=======
    # Ele vai procurar na pasta templates que configuramos no settings.py
>>>>>>> 1cea6da5e9c6ae1a5fcfbe83fecbbd074ab1453d
    return render(request, 'index.html')
