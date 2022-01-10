from django.db import models

class Uzytkownik(models.Model):
    nazwisko = models.CharField(max_length=45)
    imie = models.CharField(max_length=45)
    id_pracownika = models.CharField(max_length=12)
    jednostka_organizacyjna = models.ForeignKey('jednostka_organizacyjna.Jednostka_Organizacyjna', on_delete=models.CASCADE, null=True, blank=True)
