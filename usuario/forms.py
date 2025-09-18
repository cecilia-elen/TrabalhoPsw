from django import forms
from .models import Usuario
<<<<<<< HEAD
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm

# Placeholders para ajudar o usuário (no formulário de cadastro)
class UsuarioForm(UserCreationForm):
    # Campo extra para o formulário de criação
    cpf = forms.CharField(label="CPF", max_length=14)
    first_name = forms.CharField(label="Nome", max_length=150)
    last_name = forms.CharField(label="Sobrenome", max_length=150)

=======
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 60e0c3e232c3b9522bac92c41a6682a34c1e7220
       # Placeholders para ajudar o usuário (no formulário de cadastro)
class UsuarioForm(UserCreationForm):
>>>>>>> 8750437900de8beadd7384be3adc93d797d65d08
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
<<<<<<< HEAD
        #apenas os campos essenciais para cadastro
        fields = ('username', 'first_name', 'last_name', 'email', 'cpf')

    def save(self, commit=True):
        # Cria o User
        user = super().save(commit=True)

        # Acessamos a o cadastro inicial e os dados que faltam sao preenchidos 
        user.usuario.cpf = self.cleaned_data['cpf']
        user.usuario.first_name = self.cleaned_data['first_name']
        user.usuario.last_name = self.cleaned_data['last_name']
        user.usuario.email = self.cleaned_data['email']
        
        # Salvamos as novas informações.
        if commit:
            user.usuario.save()

        return user
=======
        #apenas os campos essenciais para cadastro, sem que o usuário perca muito tempo criando uma conta na plataforma
        fields = ('first_name', 'last_name', 'email', 'cpf')

    # --- Para que o nome do usuário seja colocado ao criar o perfil
<<<<<<< HEAD
=======
=======
class UsuarioForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ('first_name', 'last_name', 'email', 'cpf')

    # --- Para que o nome do usuário seja colocado ao criar o perfil ---
>>>>>>> 1cea6da5e9c6ae1a5fcfbe83fecbbd074ab1453d
>>>>>>> 60e0c3e232c3b9522bac92c41a6682a34c1e7220
    def save(self, commit=True):
        # Pega o objeto do usuário criado pelo formulário, mas não salva no banco ainda.
        user = super().save(commit=False)
        # Define o username para ser igual ao email.
        user.username = user.email
        if commit:
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 60e0c3e232c3b9522bac92c41a6682a34c1e7220
            # Agora salva o usuário no banco de dados com o nome preenchido.
            user.save()
        return user



class AdminUsuarioForm(forms.ModelForm):
    # Campo de senha opcional L(pq vai que a pessoa não precisa mexer com a senha, deixa a mesma)
    senha = forms.CharField(widget=forms.PasswordInput, required=False, help_text="Deixe em branco para não alterar a senha.")

    class Meta:
        model = Usuario
        # Apenas os campos que o admin pode editar
        fields = ('first_name', 'last_name', 'email', 'cpf')

    def save(self, commit=True):
        usuario = super().save(commit=False)
        nova_senha = self.cleaned_data.get("senha")
        if nova_senha:
            usuario.set_password(nova_senha)
        if commit:
            usuario.save()
        return usuario
>>>>>>> 8750437900de8beadd7384be3adc93d797d65d08

class LoginForm(AuthenticationForm):
    pass

<<<<<<< HEAD
class UsuarioUpdateForm(forms.ModelForm):
    foto_perfil = forms.ImageField(label="Foto de Perfil", required=False, widget=forms.ClearableFileInput)
    
    class Meta:
        model = Usuario
        # Todos os outros campos do perfil
        fields = ('foto_perfil', 'sobre', 'Telefone', 'estado', 'cidade', 'bairro', 'logradouro', 'numero', 'detalhamento','X', 'Facebook', 'Instagram', 'Youtube', 'Github', 'LinkedIn', 'Kwai', 'Tiktok', 'Telegram', 'Whatsapp')

    #método para atualizar blob
    def save(self, commit=True):
        instance = super().save(commit=False)
        if 'foto_perfil' in self.changed_data:
            foto = self.cleaned_data.get('foto_perfil')
            if foto:
            # Se for um arquivo novo, lê os bytes e salva
                instance.foto_perfil = foto.read()
            else:
            # Se o campo foi limpo pelo usuário, define como nulo
                instance.foto_perfil = None
            # Salva a instância no banco de dados se commit=True
        if commit:
            instance.save()
    
        return instance
        

    #Coloquei assim porque se colocassemos no models daria problema na hora de cadastrar... barraria 
=======










class UsuarioUpdateForm(forms.ModelForm):
    class Meta:
        model = Usuario
        # Todos os outros campos do perfil, tem que preencher pelo menos o endereço dele pra poder vender
        fields = ('foto_perfil', 'sobre', 'Telefone', 'estado', 'cidade', 'bairro', 'logradouro', 'numero', 'detalhamento','X', 'Facebook', 'Instagram', 'Youtube', 'Github', 'LinkedIn', 'Kwai', 'Tiktok', 'Telegram', 'Whatsapp')


#Coloquei assim porque se colocassemos no models daria problema na hora de cadastrar... barraria 
>>>>>>> 8750437900de8beadd7384be3adc93d797d65d08
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Define quais campos serão obrigatórios no formulário
        self.fields['sobre'].required = True
        self.fields['estado'].required = True
        self.fields['cidade'].required = True
        self.fields['bairro'].required = True
        self.fields['logradouro'].required = True
        self.fields['numero'].required = True
    
    def clean(self):
        #para garantir que pelo menos um campo de contato foi preenchido.
        cleaned_data = super().clean()
<<<<<<< HEAD
        campos_de_contato = ['Telefone', 'Instagram', 'Facebook', 'X', 'Youtube', 'Github','LinkedIn', 'Kwai', 'Tiktok', 'Telegram', 'Whatsapp']
        contato_preenchido = any(cleaned_data.get(campo) for campo in campos_de_contato)

        if not contato_preenchido:
=======
        
        campos_de_contato = ['Telefone', 'Instagram', 'Facebook', 'X', 'Youtube', 'Github','LinkedIn', 'Kwai', 'Tiktok', 'Telegram', 'Whatsapp']
        
        # Verifica se pelo menos um dos campos de contato tem valor
        contato_preenchido = any(cleaned_data.get(campo) for campo in campos_de_contato)

        if not contato_preenchido:
            # Se nenhum foi preenchido, lança um erro de validação
>>>>>>> 8750437900de8beadd7384be3adc93d797d65d08
            raise forms.ValidationError(
                "Para garantir que possam entrar em contato com você, por favor, preencha pelo menos uma forma de contato.",
                code='sem_contatos_sociais'
            )
<<<<<<< HEAD
        return cleaned_data
    

#formulário pro adm mudar os dados que o usuário nao pode mudar 
class AdminUsuarioUpdateForm(forms.ModelForm):

    class Meta:
        model = Usuario
        # A lista de campos que o admin pode editar
        fields = ('username', 'first_name', 'last_name', 'email', 'cpf')
#
=======
            
<<<<<<< HEAD
        return cleaned_data
=======
        return cleaned_data
=======
            # Agora salva o usuário no banco de dados com o username preenchido.
            user.save()
        return user

class LoginForm(AuthenticationForm):
    pass
>>>>>>> 1cea6da5e9c6ae1a5fcfbe83fecbbd074ab1453d
>>>>>>> 60e0c3e232c3b9522bac92c41a6682a34c1e7220
>>>>>>> 8750437900de8beadd7384be3adc93d797d65d08
