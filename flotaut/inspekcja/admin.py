from django.contrib import admin
from .models import Inspekcja

#admin.site.register(Inspekcja)

@admin.register(Inspekcja)
class InspekcjaAdmin(admin.ModelAdmin):
    # fields = ['xxx', 'yyy'] # w adminie widoczne tylko te
    # exclude = ['xxx'] # w adminie widoczne wszystkie z wyjątkiem
    list_display = ['pojazd', 'data_inspekcji']
    list_filter = ['pojazd__jednostka_organizacyjna__nazwa', 'pojazd__uzytkownik__nazwisko']
    search_fields = ['pojazd__numer_rejestracyjny']

