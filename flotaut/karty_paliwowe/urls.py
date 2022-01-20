from django.urls import path
from karty_paliwowe.views import wykaz

urlpatterns = [
    path('wykaz/', wykaz, name="wszystkie_karty")
]
