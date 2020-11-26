from django import forms
from .models import Publicacione, Autor

class Publicacionesform(forms.ModelForm):
    class Meta:
        model = Publicacione
        fields ='__all__'
        exclude = ['reaccion']