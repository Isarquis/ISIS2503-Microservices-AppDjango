from django.db import models

class Estudiante(models.Model):
    id=models.AutoField(primary_key=True, default=1)
    nombre=models.CharField(max_length=60)    
    grado=models.IntegerField()
    colegio=models.IntegerField(null=False, default=None)
    correo=models.CharField(max_length=60,null=True,blank=True)
    
    def __str__(self) -> str:
        return f"ID: {self.id}, Nombre: {self.nombre}, Grado: {self.grado}, Colegio: {self.colegio}, Correo: {self.correo}"