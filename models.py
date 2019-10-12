from django.db import models

# Create your models here.


class Miembro(models.Model):
    ApellidoPaterno = models.CharField(max_length=35)
    ApellidoMaterno = models.CharField(max_length=35)
    Nombres = models.CharField(max_length=35)
    DPI = models.CharField(max_length=13)
    FechaNacimiento = models.DateField()
    SEXOS = (('F', 'Femenino'), ('M', 'Masculino'))
    Sexo = models.CharField(max_length=1, choices=SEXOS, default='M')

    def NombreCompleto(self):
        cadena = "{0} {1}, {2}"
        return cadena.format(self.ApellidoPaterno, self.ApellidoMaterno, self.Nombres)

    def __str__(self):
        return self.NombreCompleto()


class Comunidades(models.Model):
    Nombre = models.CharField(max_length=50)
    UbicacionDepartamento = models.CharField(max_length=50)
    Coordinador = models.CharField(max_length=50)
    Estado = models.BooleanField(default=True)

    def __str__(self):
        return "{0} ({1})".format(self.Nombre, self.UbicacionDepartamento, self.Coordinador)


class Actividades(models.Model):
    NombreActividad = models.CharField(max_length=50)
    Miembro = models.ForeignKey(Miembro, null=False, blank=False, on_delete=models.CASCADE)
    Comunidades = models.ForeignKey(Comunidades, null=False, blank=False, on_delete=models.CASCADE)
    FechaActividades = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        cadena = "{0} => {3}"
        return cadena.format(self.Miembro, self.Comunidades.Nombre, self.NombreActividad, self.FechaActividades)
