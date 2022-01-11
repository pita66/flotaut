from django.db import models

class Karty_Paliwowe(models.Model):
    wystawca_karty = models.CharField(max_length=45, blank=False)
    numer_karty = models.IntegerField(blank=False)
    data_waznosci_karty = models.DateField(blank=True)
    pojazd = models.ForeignKey('pojazd.Pojazd', on_delete=models.CASCADE, null=True, blank=True)
    jednostka_organizacyjna = models.ForeignKey('jednostka_organizacyjna.Jednostka_Organizacyjna',
                                                on_delete=models.CASCADE, null=True, blank=True)
    uzytkownik = models.ForeignKey('uzytkownik.Uzytkownik', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.numer_karty}'