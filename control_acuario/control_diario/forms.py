from django import forms
from .models import Parametros_diarios

class ParametrosDiariosForm(forms.ModelForm):
    class Meta:
        model = Parametros_diarios
        fields = ['fecha', 'salinidad', 'nitrato', 'fosfato', 'nitrito', 'amonio', 'kh', 'calcio', 'magnesio']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        # Obtenemos el usuario del kwargs y lo eliminamos para no interferir con el __init__ original
        user = kwargs.pop('user', None)
        super(ParametrosDiariosForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['usuario'].initial = user
            self.fields['usuario'].widget.attrs['readonly'] = True