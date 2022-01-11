from django.db import models

class Ubezpieczenie(models.Model):

    OC = 'OC'
    AC = 'AC'
    ZIELONA_KARTA = 'ZIELONA_KARTA'
    rodzaj_polisy_wybor = [
        (OC, 'OC'),
        (AC, 'AC'),
        (ZIELONA_KARTA, 'ZIELONA_KARTA')
    ]

    ubezpieczyciel = models.CharField(max_length=45)
    rodzaj_polisy = models.CharField(max_length=45, choices=rodzaj_polisy_wybor)
    numer_polisy = models.CharField(max_length=45)
    data_poczatku_ubezpiezenie = models.DateField()
    data_konca_ubezpieczenia = models.DateField()
    pojazd = models.ForeignKey('pojazd.Pojazd', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.numer_polisy} / {self.pojazd.numer_rejestracyjny}'