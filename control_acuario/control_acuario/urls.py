"""
URL configuration for control_acuario project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Una vista simple para la página principal (solo como ejemplo)
def home_view(request):
    return HttpResponse('<h1>Bienvenido a Control de Acuario</h1>')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('control_diario/', include('control_diario.urls')),  # Cambia según tu aplicación
    path('', home_view),  # Agrega una vista para la URL raíz
]