from django import forms
from .models import Paramatros_diarios

class ParamatrosDiariosForm(forms.ModelForm):
    class Meta:
        model = Paramatros_diarios
        fields = ['fecha', 'salinidad', 'nitrato', 'fosfato', 'nitrito', 'amonio', 'kh', 'calcio', 'magnesio']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),  # Widget para la selección de fecha
        }
