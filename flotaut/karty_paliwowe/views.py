from django.shortcuts import render
from django.http import HttpResponse

def wykaz(request):
    # return HttpResponse('<h1>To jest pierwszy test</h1>')
    return render(request, 'karty_paliwowe.html')
