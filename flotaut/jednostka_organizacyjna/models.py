from django.db import models

class Jednostka_Organizacyjna(models.Model):
    nazwa = models.CharField(max_length=45)
    kod_pocztowy = models.CharField(max_length=6)
    miejscowosc = models.CharField(max_length=45)
    ulica = models.CharField(max_length=45)
    numer_domu = models.CharField(max_length=12)

    def __str__(self):
        return self.nazwa