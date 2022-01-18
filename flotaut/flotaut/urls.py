from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jednostka_organizacyjna/', include('jednostka_organizacyjna.urls')),
    path('uzytkownik/', include('uzytkownik.urls')),
    path('pojazd/', include('pojazd.urls')),
    path('ubezpieczenie/', include('ubezpieczenie.urls')),
    path('karty_paliwowe/', include('karty_paliwowe.urls')),
    path('inspekcja/', include('inspekcja.urls')),
    path('badanie_techniczne/', include('badanie_techniczne.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
