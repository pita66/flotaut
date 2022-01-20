from django.urls import path
from jednostka_organizacyjna.views import wszystkie_jednostki, nowa_jednostka, edytuj_jednostke, usun_jednostke

urlpatterns = [
    path('wykaz/', wszystkie_jednostki, name="wszystkie_jednostki"),
    path('nowa/', nowa_jednostka, name="nowa_jednostka"),
    path('edytuj/<int:id>', edytuj_jednostke, name="edytuj_jednostke"),
    path('usun/<int:id>', usun_jednostke, name="usun_jednostke"),
]
