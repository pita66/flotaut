from django.urls import path
from pojazd.views import wszystkie_pojazdy, nowy_pojazd, edytuj_pojazd, usun_pojazd

urlpatterns = [
    path('wykaz/', wszystkie_pojazdy, name="wszystkie_pojazdy"),
    path('nowy/', nowy_pojazd, name="nowy_pojazd"),
    path('edytuj/<int:id>/', edytuj_pojazd, name="edytuj_pojazd"),
    path('usun/<int:id>/', usun_pojazd, name="usun_pojazd")
]
