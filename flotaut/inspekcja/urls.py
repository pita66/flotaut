from django.urls import path
from inspekcja.views import wykaz

urlpatterns = [
    path('wykaz/', wykaz, name="wszystkie_inspekcje")
]
