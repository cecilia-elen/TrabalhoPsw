from django import forms
from .models import Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
<<<<<<< HEAD
        fields = ('nome', 'cat_pai')
=======
        fields = ('nome', 'categoria_pai')
>>>>>>> 8750437900de8beadd7384be3adc93d797d65d08

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Este trecho torna o campo 'categoria_pai' opcional no formulário
      
<<<<<<< HEAD
#
=======
>>>>>>> 8750437900de8beadd7384be3adc93d797d65d08
