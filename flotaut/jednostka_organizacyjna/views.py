from django.shortcuts import render
from .models import Jednostka_Organizacyjna
from django.http import HttpResponse

def wykaz(request):
    wykaz_jednostka_organizacyjna = Jednostka_Organizacyjna.objects.all()
    #wykaz_jednostka_organizacyjna = [] # testowanie braku jednostek organizacyjnych
    return render(request, 'jednostka_organizacyjna.html', {'jednostka_organizacyjna': wykaz_jednostka_organizacyjna})
