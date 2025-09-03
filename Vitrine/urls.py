from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Quando alguém acessar o site principal (''), chame a função 'pagina_inicial'
    path('', views.pagina_inicial, name='pagina-inicial'),
    path('usuario/', include('usuario.urls')),
    path('catalogo/', include('catalogo.urls')),
    path('categoria/', include('categoria.urls')),
    path('produtos/', include('produto.urls')),
    path('empresa/', include('empresa.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)