from django.urls import path
from jednostka_organizacyjna.views import wykaz

urlpatterns = [
    path('wykaz/', wykaz)
]
