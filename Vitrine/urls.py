from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
from . import views
from django.conf import settings
from django.conf.urls.static import static
=======
from . import views 
>>>>>>> 1cea6da5e9c6ae1a5fcfbe83fecbbd074ab1453d

urlpatterns = [
    path('admin/', admin.site.urls),
    # Quando alguém acessar o site principal (''), chame a função 'pagina_inicial'
    path('', views.pagina_inicial, name='pagina-inicial'),
    path('usuario/', include('usuario.urls')),
<<<<<<< HEAD
    path('catalogo/', include('catalogo.urls')),
    path('categoria/', include('categoria.urls')),
    path('produtos/', include('produto.urls')),
    path('empresa/', include('empresa.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
    path('ADM/', include('dashboard.urls')),

    # As URLs para seus outros apps (produto, etc.) virão aqui depois
]
>>>>>>> 1cea6da5e9c6ae1a5fcfbe83fecbbd074ab1453d
