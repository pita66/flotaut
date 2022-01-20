from django.urls import path
from badanie_techniczne.views import wykaz

urlpatterns = [
    path('wykaz/', wykaz, name='wszystkie_badania')
]
