from django.shortcuts import render

from django.shortcuts import render
from .forms import ParamatrosDiariosForm

def formulario_view(request):
    if request.method == 'POST':
        form = ParamatrosDiariosForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ParamatrosDiariosForm()

    return render(request, 'formulario.html', {'form': form})

