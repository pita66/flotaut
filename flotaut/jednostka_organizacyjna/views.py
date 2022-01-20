from django.shortcuts import render, get_object_or_404, redirect
from .models import Jednostka_Organizacyjna
from .forms import JednostkaForm
from django.contrib.auth.decorators import login_required

# Read

def wszystkie_jednostki(request):
    wykaz_jednostka_organizacyjna = Jednostka_Organizacyjna.objects.all()
    return render(request, 'jednostka_organizacyjna.html', {'jednostka_organizacyjna': wykaz_jednostka_organizacyjna})

# Create

@login_required()
def nowa_jednostka(request):
    form = JednostkaForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(wszystkie_jednostki)

    return render(request, 'jednostka_form.html', {'form': form, 'nowa_jednostka': True})

# Update

@login_required()
def edytuj_jednostke(request, id):
    jednostka_organizacyjna = get_object_or_404(Jednostka_Organizacyjna, pk=id)
    form = JednostkaForm(request.POST or None, request.FILES or None, instance=jednostka_organizacyjna)

    if form.is_valid():
        form.save()
        return redirect(wszystkie_jednostki)

    return render(request, 'jednostka_form.html', {'form': form, 'nowa_jednostka': False})

# Delete

@login_required()
def usun_jednostke(request, id):
    jednostka_organizacyjna = get_object_or_404(Jednostka_Organizacyjna, pk=id)

    if request.method == "POST":
        jednostka_organizacyjna.delete()
        return redirect(wszystkie_jednostki)

    return render(request, 'potwierdz_usun_jednostke.html', {'jednostka_organizacyjna': jednostka_organizacyjna})