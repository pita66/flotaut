from django.shortcuts import render, get_object_or_404, redirect
from .models import Pojazd
from .forms import PojazdForm
from django.contrib.auth.decorators import login_required



# Read

def wszystkie_pojazdy(request):
    wykaz_pojazd = Pojazd.objects.all()
    return render(request, 'pojazd.html', {'pojazd': wykaz_pojazd})

# Create

@login_required()
def nowy_pojazd(request):
    form = PojazdForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(wszystkie_pojazdy)

    return render(request, 'pojazd_form.html', {'form': form})

# Update

@login_required()
def edytuj_pojazd(request, id):
    pojazd = get_object_or_404(Pojazd, pk=id)
    form = PojazdForm(request.POST or None, request.FILES or None, instance=pojazd)

    if form.is_valid():
        form.save()
        return redirect(wszystkie_pojazdy)

    return render(request, 'pojazd_form.html', {'form': form})

# Delete

@login_required()
def usun_pojazd(request, id):
    pojazd = get_object_or_404(Pojazd, pk=id)

    if request.method == "POST":
        pojazd.delete()
        return redirect(wszystkie_pojazdy)

    return render(request, 'potwierdz_usun_pojazd.html', {'pojazd': pojazd})