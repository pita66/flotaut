from django.db import models

class Ubezpieczenie(models.Model):
    ubezpieczyciel = models.CharField(max_length=45)
    rodzaj_polisy = models.CharField(max_length=45)
    numer_polisy = models.CharField(max_length=45)
    data_poczatku_ubezpiezenie = models.DateField()
    data_konca_ubezpieczenia = models.DateField()
    pojazd = models.ForeignKey('pojazd.Pojazd', on_delete=models.CASCADE, null=True, blank=True)
