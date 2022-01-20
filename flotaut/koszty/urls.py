from django.urls import path
from koszty.views import wykaz

urlpatterns = [
    path('wykaz/', wykaz, name="wszystkie_koszty")
]