from django.contrib.auth.models import User#Importamos el modelo User
from django.contrib.auth.forms import UserCreationForm#Importamos el form UserCreationForm

#Clase RegistroForm hereda de UserCreationForm
class RegistroForm(UserCreationForm):

	class Meta:
		model = User
		fields = [
				'username',
				'first_name',
				'last_name',
				'email',
			] 
		labels = {
				'username': 'Nombre de Usuario',
				'first_name': 'Nombre',
				'last_name': 'Apellidos',
				'email': 'Correo',
			} 
