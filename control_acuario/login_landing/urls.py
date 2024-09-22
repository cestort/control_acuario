from django.urls import path
from . import views

app_name = 'login_landing'  # Define el namespace para esta aplicación

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
    path('', views.landingpage_view, name='landingpage'),
]
