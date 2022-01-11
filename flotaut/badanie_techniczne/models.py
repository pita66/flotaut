from django.db import models

class Badanie_Techniczne(models.Model):
    data_badania = models.DateField()
    stan_licznika = models.IntegerField()
    data_nastepnego_badania = models.DateField()
    pojazd = models.ForeignKey('pojazd.Pojazd', on_delete=models.CASCADE, null=True, blank=True)
