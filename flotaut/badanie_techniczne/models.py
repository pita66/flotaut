from django.db import models

class Badanie_Techniczne(models.Model):
    data_badania = models.DateField()
    stan_licznika = models.IntegerField()
    data_nastepnego_badania = models.DateField()
    pojazd = models.ForeignKey('pojazd.Pojazd', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        #return self.pojazd.numer_rejestracyjny # inne rozwiązanie
        return f'{self.pojazd.numer_rejestracyjny} / {self.data_nastepnego_badania}'