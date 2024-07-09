from django.db import models

class Vehiculo(models.Model):
    patente = models.CharField(max_length=6, primary_key=True)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.patente} - {self.marca} {self.modelo} ({self.year})"

class Chofer(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now_add=True)
    vehiculo = models.OneToOneField(Vehiculo, null=True, blank=True, on_delete=models.SET_NULL, unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.rut})"

class RegistroContabilidad(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_compra = models.DateField()
    valor = models.FloatField()
    vehiculo = models.OneToOneField(Vehiculo, on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return f"Registro {self.id} - Vehículo {self.vehiculo.patente}"
