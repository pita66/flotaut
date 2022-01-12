from django.contrib import admin
from .models import Pojazd

#admin.site.register(Pojazd)

@admin.register(Pojazd)
class PojazdAdmin(admin.ModelAdmin):
    # fields = ['xxx', 'yyy'] # w adminie widoczne tylko te
    # exclude = ['xxx'] # w adminie widoczne wszystkie z wyjątkiem
    list_display = ['numer_rejestracyjny', 'marka', 'model', 'jednostka_organizacyjna', 'uzytkownik']
    list_filter = ['jednostka_organizacyjna', 'uzytkownik', 'rodzaj']
    search_fields = ['numer_rejestracyjny']
