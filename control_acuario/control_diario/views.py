from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ParametrosDiariosForm

@login_required
def formulario_view(request):
    if request.method == 'POST':
        form = ParametrosDiariosForm(request.POST)
        if form.is_valid():
            datos = form.save(commit=False)
            datos.usuario = request.user  # Asignamos el usuario actual
            datos.save()
            messages.success(request, 'Los parámetros han sido guardados exitosamente.')
            return redirect('control_diario:lista_datos')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = ParametrosDiariosForm()
    return render(request, 'control_diario/formulario.html', {'form': form})
