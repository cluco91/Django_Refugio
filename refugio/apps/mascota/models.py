from django.db import models

from apps.adopciones.models import Persona
# Create your models here.


class Vacuna(models.Model):
	nombre = models.CharField(max_length=50)

	def __str__(self): 
		return '{}'.format(self.nombre)


#Mascota extiende de Model, por eso, al igual que con todos los 
#modelos que creemos debemos colocar entre parentesis models.Model

class Mascota(models.Model): 
	#atributos o campos
	#a nombre le asignamos el tipo de dato o de campo
	#etc
	#folio = models.CharField(max_length=10, primary_key=True)
	nombre = models.CharField(max_length=50)
	sexo = models.CharField(max_length=10)
	edad_aproximada = models.IntegerField()
	fecha_rescate = models.DateField()
	persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE) #Llave Foranea
	vacuna = models.ManyToManyField(Vacuna, blank=True) #Muchos a Muchos


