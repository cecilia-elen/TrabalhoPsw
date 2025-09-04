from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

       # Placeholders para ajudar o usuário (no formulário de cadastro)
class UsuarioForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = "Senha"
        self.fields['password2'].label = "Confirmação de senha"
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Seu primeiro nome'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Seu sobrenome'})
        self.fields['email'].widget.attrs.update({'placeholder': 'seuemail@exemplo.com'})
        self.fields['cpf'].widget.attrs.update({'placeholder': '000.000.000-00'})

    class Meta(UserCreationForm.Meta):
        model = Usuario
        #apenas os campos essenciais para cadastro, sem que o usuário perca muito tempo criando uma conta na plataforma
        fields = ('first_name', 'last_name', 'email', 'cpf')

    # --- Para que o nome do usuário seja colocado ao criar o perfil
    def save(self, commit=True):
        # Pega o objeto do usuário criado pelo formulário, mas não salva no banco ainda.
        user = super().save(commit=False)
        # Define o username para ser igual ao email.
        user.username = user.email
        if commit:
            # Agora salva o usuário no banco de dados com o nome preenchido.
            user.save()
        return user

class LoginForm(AuthenticationForm):
    pass











class UsuarioUpdateForm(forms.ModelForm):
    class Meta:
        model = Usuario
        # Todos os outros campos do perfil, tem que preencher pelo menos o endereço dele pra poder vender
        fields = ('foto_perfil', 'sobre', 'Telefone', 'estado', 'cidade', 'bairro', 'endereco', 'numero', 'detalhamento','X', 'Facebook', 'Instagram', 'Youtube', 'Github', 'LinkedIn', 'Kwai', 'Tiktok', 'Telegram', 'Whatsapp')


#Coloquei assim porque se colocassemos no models daria problema na hora de cadastrar... barraria 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Define quais campos serão obrigatórios no formulário
        self.fields['sobre'].required = True
        self.fields['estado'].required = True
        self.fields['cidade'].required = True
        self.fields['bairro'].required = True
        self.fields['endereco'].required = True
        self.fields['numero'].required = True
    
    def clean(self):
        #para garantir que pelo menos um campo de contato foi preenchido.
        cleaned_data = super().clean()
        
        campos_de_contato = ['Telefone', 'Instagram', 'Facebook', 'X', 'Youtube', 'Github','LinkedIn', 'Kwai', 'Tiktok', 'Telegram', 'Whatsapp']
        
        # Verifica se pelo menos um dos campos de contato tem valor
        contato_preenchido = any(cleaned_data.get(campo) for campo in campos_de_contato)

        if not contato_preenchido:
            # Se nenhum foi preenchido, lança um erro de validação
            raise forms.ValidationError(
                "Para garantir que possam entrar em contato com você, por favor, preencha pelo menos uma forma de contato.",
                code='sem_contatos_sociais'
            )
            
        return cleaned_data