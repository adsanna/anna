
from django import forms
from .models import Documentos

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documentos
        fields = ['titulo', 'descricao', 'departamento', 'arquivo']
