from django.contrib import admin
from .models import Ubezpieczenie

#admin.site.register(Ubezpieczenie)

@admin.register(Ubezpieczenie)
class UbezpieczenieAdmin(admin.ModelAdmin):
    # fields = ['xxx', 'yyy'] # w adminie widoczne tylko te
    # exclude = ['xxx'] # w adminie widoczne wszystkie z wyjątkiem
    list_display = ['numer_polisy', 'pojazd', 'rodzaj_polisy', 'data_konca_ubezpieczenia']
    list_filter = ['pojazd', 'rodzaj_polisy']
    search_fields = ['numer_polisy', 'pojazd__numer_rejestracyjny']