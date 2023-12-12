from django import forms
from .models import EstatuaSimplificada

class EstatuaSimplificadaForm(forms.ModelForm):
   class Meta:
       model = EstatuaSimplificada
       fields = ['nombre', 'id', 'descripcion', 'modelo', 'ubicacion']