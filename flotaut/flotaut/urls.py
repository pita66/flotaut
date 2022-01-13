from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jednostka_organizacyjna/', include('jednostka_organizacyjna.urls')),
    path('uzytkownik/', include('uzytkownik.urls')),
    path('pojazd/', include('pojazd.urls')),
    path('ubezpieczenie/', include('ubezpieczenie.urls')),
    path('karty_paliwowe/', include('karty_paliwowe.urls')),
    path('inspekcja/', include('inspekcja.urls')),
    path('badanie_techniczne/', include('badanie_techniczne.urls'))
]
