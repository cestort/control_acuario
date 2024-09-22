from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login
from django.urls import reverse  # Importa reverse para generar URLs

# Vista para la página principal o landing page
def landingpage_view(request):
    return render(request, 'login_landing/landingpage.html')

# Vista para el login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(reverse('control_diario:formulario'))  # Usa reverse con namespace
    else:
        form = AuthenticationForm()

    return render(request, 'login_landing/login.html', {'form': form})

# Vista para el registro de usuarios
def registro_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Autenticamos automáticamente después de registrar
            return redirect(reverse('control_diario:formulario'))  # Usa reverse con namespace
    else:
        form = UserCreationForm()

    return render(request, 'login_landing/registro.html', {'form': form})
