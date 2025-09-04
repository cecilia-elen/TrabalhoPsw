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
