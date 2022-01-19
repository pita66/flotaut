from django.forms import ModelForm
from .models import Pojazd

class PojazdForm(ModelForm):
    class Meta:
        model = Pojazd
        fields = ['numer_rejestracyjny',
                  'marka',
                  'typ',
                  'model',
                  'rodzaj',
                  'podrodzaj',
                  'kategoria',
                  'rok_produkcji',
                  'data_pierwszej_rejestracji',
                  'numer_vin',
                  'przeznaczenie',
                  'numer_dowodu_rejestracyjnego',
                  'numer_karty_pojazdu',
                  'organ_wydajacy',
                  'numer_swiadectwa_homologacji',
                  'rodzaj_paliwa',
                  'liczba_miejsc',
                  'hak',
                  'pojemnosc_silnika',
                  'moc_silnika',
                  'masa_wlasna',
                  'masa_calkowita',
                  'ladownosc',
                  'jednostka_organizacyjna',
                  'uzytkownik',
                  'zdjecie',
                  ]