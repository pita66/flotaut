from django.db import models

class Inspekcja(models.Model):

    letnie = 'L'
    zimowe = 'Z'
    wielosezonowe = 'W'
    ogumienie_rodzaj_wybor = [
        (letnie, 'letnie'),
        (zimowe, 'zimowe'),
        (wielosezonowe, 'wielosezonowe')
    ]

    dobry = 'dobry'
    dopuszczalny = 'dopuszczalny'
    zly = 'zly'
    ogumienie_stan_wybor = [
        (dobry, 'dobry'),
        (dopuszczalny, 'dopuszczalny'),
        (zly, 'zly')
    ]

    sprawne = 'sprawne'
    niesprawne = 'niesprawne'
    oswietlenie_wybor = [
        (sprawne, 'sprawne'),
        (niesprawne, 'niesprawne')
    ]

    uszkodzone = 'uszkodzone'
    nieuszkodzone = 'nieuszkodzone'
    szyby_lusterka_wybor = [
        (uszkodzone, 'uszkodzone'),
        (nieuszkodzone, 'nieuszkodzone')
    ]

    uszkodzone = 'uszkodzone'
    nieuszkodzone = 'nieuszkodzone'
    nadwozie_wybor = [
        (uszkodzone, 'uszkodzone'),
        (nieuszkodzone, 'nieuszkodzone')
    ]

    sprawny = 'sprawny'
    niesprawny = 'niesprawny'
    silnik_wybor = [
        (sprawny, 'sprawny'),
        (niesprawny, 'niesprawny')
    ]

    uszkodzone = 'uszkodzone'
    nieuszkodzone = 'nieuszkodzone'
    wnetrze_wybor = [
        (uszkodzone, 'uszkodzone'),
        (nieuszkodzone, 'nieuszkodzone')
    ]

    kompletne = 'kompletne'
    niekompletne = 'niekompletne'
    wyposazenie_wybor = [
        (kompletne, 'kompletne'),
        (niekompletne, 'niekompletne')
    ]

    pojazd = models.ForeignKey('pojazd.Pojazd', on_delete=models.CASCADE, null=True, blank=True)
    uzytkownik = models.ForeignKey('uzytkownik.Uzytkownik', on_delete=models.CASCADE, null=True, blank=True)
    data_inspekcji = models.DateField()
    stan_licznika = models.IntegerField()
    ogumienie_rodzaj = models.CharField(max_length=24, choices=ogumienie_rodzaj_wybor, blank=False)
    ogumienie_stan = models.CharField(max_length=24, choices=ogumienie_stan_wybor, blank=False)
    oswietlenie = models.CharField(max_length=24, choices=oswietlenie_wybor, blank=False)
    szyby_lusterka = models.CharField(max_length=24, choices=szyby_lusterka_wybor, blank=False)
    nadwozie = models.CharField(max_length=24, choices=nadwozie_wybor, blank=False)
    silnik = models.CharField(max_length=24, choices=silnik_wybor, blank=False)
    wnetrze = models.CharField(max_length=24, choices=wnetrze_wybor, blank=False)
    wyposazenie = models.CharField(max_length=24, choices=wyposazenie_wybor, blank=False)

    def __str__(self):
        #return self.pojazd.numer_rejestracyjny # inne rozwiązanie
        return f'{self.pojazd.numer_rejestracyjny} / {self.data_inspekcji}'
