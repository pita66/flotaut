from django.forms import ModelForm
from .models import Jednostka_Organizacyjna

class JednostkaForm(ModelForm):
    class Meta:
        model = Jednostka_Organizacyjna
        fields = ['nazwa',
                  'kod_pocztowy',
                  'miejscowosc',
                  'ulica',
                  'numer_domu'
                  ]