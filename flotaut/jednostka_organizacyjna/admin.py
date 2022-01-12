from django.contrib import admin
from .models import Jednostka_Organizacyjna

# admin.site.register(Jednostka_Organizacyjna)

@admin.register(Jednostka_Organizacyjna)
class Jednostka_OrganizacyjnaAdmin(admin.ModelAdmin):
    # fields = ['nazwa', 'miejscowosc'] # w adminie widoczne tylko te
    # exclude = ['kod_pocztowy'] # w adminie widoczne wszystkie z wyjątkiem
    list_display = ['nazwa', 'miejscowosc']
    list_filter = ['miejscowosc']
    search_fields = ['nazwa', 'miejscowosc']