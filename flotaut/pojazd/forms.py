from django.forms import ModelForm
from .models import Pojazd

class PojazdForm(ModelForm):
    class Meta:
        model = Pojazd
        fields = ['numer_rejestracyjny', 'marka', 'typ', 'model']