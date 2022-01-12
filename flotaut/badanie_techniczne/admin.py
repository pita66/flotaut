from django.contrib import admin
from .models import Badanie_Techniczne

#admin.site.register(Badanie_Techniczne)

@admin.register(Badanie_Techniczne)
class Badanie_TechniczneAdmin(admin.ModelAdmin):
    # fields = ['xxx', 'yyy'] # w adminie widoczne tylko te
    # exclude = ['xxx'] # w adminie widoczne wszystkie z wyjątkiem
    list_display = ['pojazd', 'data_nastepnego_badania']
    list_filter = ['pojazd__jednostka_organizacyjna__nazwa', 'pojazd__uzytkownik__nazwisko']
    search_fields = ['pojazd__numer_rejestracyjny']
