from django.forms import ModelForm
from app.models import Ajuda


class AjudaForm(ModelForm):
    class Meta:
        model = Ajuda
        fields = ['nome', 'telefone', 'email']
