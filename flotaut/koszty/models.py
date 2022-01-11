from django.db import models

class Koszty(models.Model):

    koszty_paliwa = 'koszty_paliwa'
    koszty_ubepieczenia = 'koszty_ubezpieczenia'
    koszty_przegladu = 'koszty_przegladu'
    koszty_naprawy = 'koszty_naprawy'
    koszty_wyposazenia = 'koszty_wyposazenia'
    inne_koszty = 'inne_koszty'
    rodzaj_kosztow_wybor = [
        (koszty_paliwa, 'koszty_paliwa'),
        (koszty_ubepieczenia, 'koszty_ubezpieczenia'),
        (koszty_przegladu, 'koszty_przegladu'),
        (koszty_naprawy, 'koszty_naprawy'),
        (koszty_wyposazenia, 'koszty_wyposazenia'),
        (inne_koszty, 'inne_koszty')
    ]

    data_powstania_kosztu = models.DateField()
    kwota_netto = models.IntegerField()
    stan_licznika = models.IntegerField()
    numer_dokumentu = models.CharField(max_length=45)
    pojazd = models.ForeignKey('pojazd.Pojazd', on_delete=models.CASCADE, null=True, blank=True)
    rodzaj_kosztow = models.CharField(max_length=45, choices=rodzaj_kosztow_wybor, blank=False)

