from django.db import models
from django.contrib.auth.models import User 

class Parametros_diarios(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Relaciona cada entrada con un usuario
    fecha = models.DateField()  # Campo para la fecha
    hora = models.TimeField(auto_now_add=True) #campo de hora autocompletante
    salinidad = models.FloatField()  # Salinidad
    nitrato = models.FloatField()  # Nitrato
    fosfato = models.FloatField()  # Fosfato
    nitrito = models.FloatField()  # Nitrito
    amonio = models.FloatField()  # Amonio
    kh = models.FloatField()  # Alcalinidad (Kh)
    calcio = models.IntegerField()  # Calcio
    magnesio = models.IntegerField()  # Magnesio

    def __str__(self):
        return f"Parámetros del {self.fecha}"

