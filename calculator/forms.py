from django import forms
from .models import ConsumoEnergia

class ConsumoEnergiaForm(forms.ModelForm):
    class Meta:
        model = ConsumoEnergia
        fields = '__all__'
