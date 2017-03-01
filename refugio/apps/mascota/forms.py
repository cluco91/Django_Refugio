from django import forms

#importo el modelo Mascota
from apps.mascota.models import Mascota

class MascotaForm(forms.ModelForm):

	class Meta:
		#De que modelo crearemos este formulario
		model = Mascota

		#Definiremos los campos del modelo
		fields = [
			'nombre',
			'sexo',
			'edad_aproximada',
			'fecha_rescate',
			'persona',
			'vacuna',
		]

		#Ahora asignamos las etiquetas que van a tener a la hora
		#de pintar el formulario

		labels = {
			#Aqui escribimos el diccionario
			'nombre': 'Nombre',
			'sexo': 'Sexo',
			'edad_aproximada': 'Edad Aproximada',
			'fecha_rescate': 'Fecha de Rescate',
			'persona': 'Adoptante',
			'vacuna': 'Vacuna',
		}

		#Aqui declaramos los widgets
		#Los widgets son los que se van a pintar a forma 
		#de etiquetas html

		widgets = {
			#A los widgets se les puede colocar los atributos de la clase, form-control es el que viene con bootstrap
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'sexo': forms.TextInput(attrs={'class':'form-control'}),
			'edad_aproximada': forms.TextInput(attrs={'class':'form-control'}),
			'fecha_rescate': forms.TextInput(attrs={'class':'form-control'}),
			#Este atributo es una llave foranea, asi que conviene que sea un Select
			'persona': forms.Select(attrs={'class':'form-control'}),
			#Este campo vacuna es un campo many to many, entonces usaremos el CheckboxSelectMultiple que nos entrega Django
			'vacuna': forms.CheckboxSelectMultiple(),
		}
		