from django.db import models

class Pojazd(models.Model):

    TAK = 'T'
    NIE = 'N'
    hak_wybor = [
        (TAK, 'TAK'),
        (NIE, 'NIE')
    ]

    Pb = 'Pb'
    ON = 'ON'
    LPG = 'Pb + LPG'
    PRZYCZEPA = 'PRZYCZEPA'
    rodzaj_paliwa_wybor = [
        (Pb, 'Pb'),
        (ON, 'ON'),
        (LPG, 'Pb + LPG'),
        (PRZYCZEPA, 'PRZYCZEPA')
    ]

    numer_rejestracyjny = models.CharField(max_length=10, blank=False)
    marka = models.CharField(max_length=45)
    typ = models.CharField(max_length=45, blank=True)
    model = models.CharField(max_length=45)
    rodzaj = models.CharField(max_length=45)
    podrodzaj = models.CharField(max_length=45, blank=True)
    kategoria = models.CharField(max_length=45, blank=True)
    rok_produkcji = models.IntegerField()
    data_pierwszej_rejestracji = models.DateField()
    numer_vin = models.CharField(max_length=24)
    przeznaczenia = models.CharField(max_length=45, blank=True)
    numer_dowodu_rejestracyjnego = models.CharField(max_length=12)
    numer_karty_pojazdu = models.CharField(max_length=12)
    organ_wydajacy = models.CharField(max_length=45)
    numer_swiadectwa_homologacji = models.CharField(max_length=45, blank=True)
    rodzaj_paliwa = models.CharField(max_length=12, choices=rodzaj_paliwa_wybor, blank=False)
    liczba_miejsc = models.IntegerField(blank=True)
    hak = models.CharField(max_length=3, choices=hak_wybor, default=NIE)
    pojemnosc_silnika = models.IntegerField(blank=True)
    moc_silnika = models.IntegerField(blank=True)
    masa_wlasna = models.IntegerField(null=True, blank=True)
    masa_calkowita = models.IntegerField(blank=True)
    ladownosc = models.IntegerField(blank=True)
    jednostka_organizacyjna = models.ForeignKey('jednostka_organizacyjna.Jednostka_Organizacyjna',
                                                on_delete=models.CASCADE, null=True, blank=True)
    uzytkownik = models.ForeignKey('uzytkownik.Uzytkownik', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.numer_rejestracyjny