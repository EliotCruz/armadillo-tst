from django.db import models

# Create your models here.
class Constancia(models.Model):
    noControl = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    apellidoPaterno = models.CharField(max_length=100)
    apellidoMaterno = models.CharField(max_length=100)
    semestre = models.CharField(max_length=10)
    claveCarrera = models.CharField(max_length=10)
    carrera = models.CharField(max_length=100)
    fechaInscripcion = models.DateField()
    horaInscripcion = models.TimeField()
    titulo = models.CharField(max_length=200)
    noConsecutivo= models.CharField(max_length=50)
    promedio = models.DecimalField(max_digits=5, decimal_places=2)
    avance = models.DecimalField(max_digits=5, decimal_places=2)
    creditosAprobados = models.DecimalField(max_digits=5, decimal_places=2)
    token = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.noControl} - {self.nombre} {self.apellidoPaterno} {self.apellidoMaterno} "
    
