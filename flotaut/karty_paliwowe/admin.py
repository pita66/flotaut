from django.contrib import admin
from .models import Karty_Paliwowe

# admin.site.register(Karty_Paliwowe)

@admin.register(Karty_Paliwowe)
class Karty_PaliwoweAdmin(admin.ModelAdmin):
    # fields = ['xxx', 'yyy'] # w adminie widoczne tylko te
    # exclude = ['xxx'] # w adminie widoczne wszystkie z wyjątkiem
    list_display = ['numer_karty', 'pojazd', 'data_waznosci_karty', 'wystawca_karty']
    list_filter = ['pojazd', 'jednostka_organizacyjna', 'uzytkownik', 'wystawca_karty']
    search_fields = ['numer_karty', 'pojazd__numer_rejestracyjny']