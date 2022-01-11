from django.db import models

class Karty_Paliwowe(models.Model):
    wystawca_karty = models.CharField(max_length=45)
    numer_karty = models.IntegerField()
    data_waznosci_karty = models.DateField()
    pojazd = models.ForeignKey('pojazd.Pojazd', on_delete=models.CASCADE, null=True, blank=True)
    jednostka_organizacyjna = models.ForeignKey('jednostka_organizacyjna.Jednostka_Organizacyjna',
                                                on_delete=models.CASCADE, null=True, blank=True)
    uzytkownik = models.ForeignKey('uzytkownik.Uzytkownik', on_delete=models.CASCADE, null=True, blank=True)

