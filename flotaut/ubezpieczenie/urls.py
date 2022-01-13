from django.urls import path
from ubezpieczenie.views import wykaz

urlpatterns = [
    path('wykaz/', wykaz)
]
