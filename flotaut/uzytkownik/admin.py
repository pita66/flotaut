from django.contrib import admin
from .models import Uzytkownik

# admin.site.register(Uzytkownik)

@admin.register(Uzytkownik)
class UzytkownikAdmin(admin.ModelAdmin):
    # fields = ['xxx', 'yyy'] # w adminie widoczne tylko te
    # exclude = ['xxx'] # w adminie widoczne wszystkie z wyjątkiem
    list_display = ['nazwisko', 'imie', 'jednostka_organizacyjna']
    list_filter = ['jednostka_organizacyjna']
    search_fields = ['nazwisko', 'imie']