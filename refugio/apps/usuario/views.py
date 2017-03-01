import json
from rest_framework.views import APIView

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User#Importamos el modelo User
from django.contrib.auth.forms import UserCreationForm#Importamos el form UserCreationForm
from django.views.generic import CreateView#Importamos la vista generica CreateView
from django.core.urlresolvers import reverse_lazy

from apps.usuario.forms import RegistroForm
from apps.usuario.serializers import UserSerializer

# Create your views here.

#RegistrarUsuario
class RegistroUsuario(CreateView):
	model = User
	template_name = "usuario/registrar.html"
	form_class = RegistroForm
	success_url = reverse_lazy('mascota:mascota_listar')

#APIView es una vista de restframework
class UserAPI(APIView):
	serializer = UserSerializer
	#Sobreescribimos el metodo get de APIView
	def get(self, request, format=None):
		lista = User.objects.all()#Obtener todos los objetos de User
		response = self.serializer(lista, many=True)#El many=True es porque nos va a devolver muchos registros

		return HttpResponse(json.dumps(response.data), content_type='application/json')



