from django.db import models

class Paramatros_diarios(models.Model):
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
