from django.urls import path
from uzytkownik.views import wykaz

urlpatterns = [
    path('wykaz/', wykaz)
]
