from django.db import models

class Jednostka_Organizacyjna(models.Model):
    nazwa = models.CharField(max_length=45, blank=False)
    kod_pocztowy = models.CharField(max_length=6, blank=True)
    miejscowosc = models.CharField(max_length=45, blank=False)
    ulica = models.CharField(max_length=45, blank=True)
    numer_domu = models.CharField(max_length=12, blank=True)

    def __str__(self):
        return self.jednostka_organizacyjna_wykaz()

    def jednostka_organizacyjna_wykaz(self):
        return '{} ({})'.format(self.nazwa, self.miejscowosc)