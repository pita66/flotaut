from django.urls import path
from pojazd.views import wykaz

urlpatterns = [
    path('wykaz/', wykaz)
]
