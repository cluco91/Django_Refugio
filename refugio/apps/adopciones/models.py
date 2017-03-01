from django.db import models

# Create your models here.

class Persona(models.Model):
	nombre = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=70)
	edad = models.IntegerField()
	telefono = models.CharField(max_length=12)
	email = models.EmailField()
	domicilio = models.TextField()

	#Agregado para que se vea el nombre de la persona en lugar de representarlo como Persona Object
	def __str__(self):
		return '{} {}'.format(self.nombre, self.apellidos) 
		#Esto hace que cuando yo acceda al objeto me retornara el atributo nombre y apellidos

#Esta solicitud la vamos a llenar con los datos de la persona.
class Solicitud(models.Model):
	persona = models.ForeignKey(Persona, null=True, blank=True)
	numero_mascotas = models.IntegerField()
	razones = models.TextField()		