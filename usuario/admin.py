from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Usuario

# Crie uma classe para exibir os campos do Perfil 'Usuario' junto com o User
class UsuarioInline(admin.StackedInline):
    model = Usuario
    can_delete = False
    verbose_name_plural = 'Perfil Detalhado'

# Defina uma nova classe de Admin para o User
class CustomUserAdmin(UserAdmin):
    inlines = (UsuarioInline,)

# Re-registre o modelo User padrão com nossa configuração customizada
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
#
