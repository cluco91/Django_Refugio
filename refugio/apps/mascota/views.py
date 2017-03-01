from django.shortcuts import render, redirect
from django.contrib.auth.models import User#Importamos el modelo User para probar la serializacion de objetos
#Esto lo importe
from django.http import HttpResponse

#Importar los serializers
from django.core import serializers

#Agrego el urlresolver reverse_lazy
from django.core.urlresolvers import reverse_lazy

#Agregamos el view ListView de django
from django.views.generic import ListView, CreateView, UpdateView,DeleteView

#Importamos el formulario MascotaForm
from apps.mascota.forms import MascotaForm

#Importamos el modelo Mascota de apps/mascota/models.py
from apps.mascota.models import Mascota



def listadousuarios(request):
	lista = serializers.serialize('json', User.objects.all(), fields=['username','first_name'])#esta variable nos serializara los objetos
#El queryset Mascota.objects.all() traerá todos los objetos de Modelo Mascota.
	return HttpResponse(lista, content_type='application/json')#devuelve la lista


# Create your views here.
def index(request):
	return render(request, 'mascota/index.html') # render es un shortcut que recibe dos parametros: el request y el nombre de la plantilla

#vista basada en funcion, antes era solo vista basada en funcion
#pero despues veremos las vistas basadas en clase que es algo más
#nuevo para Django
def mascota_view(request):
#Si el metodo que recibe la peticion (osease request) es un POST, entonces se van a recibir
#los datos que se están mandando en el POST de nuestro formulario
	if request.method == 'POST':
		form = MascotaForm(request.POST)
		#Si lo que se recibe es un POST, preguntaremos si los datos son validos
		if form.is_valid():
			#si los datos son validos se guardaran los datos en el formulario
			form.save()
		#Despues de guardar los datos somos redirigidos a una url
		#Esa url será el index de mascota
		return redirect('mascota:mascota_listar')
		#Si no es un metodo POST le vamos a decir que nos vuelva a renderizar el formulario.
	else:
		#Esto lo usaremos cuando el metodo de envio sea un GET
		form = MascotaForm()

		#Por ultimo le mandariamos la respuesta que llevaría un request, el nombre del template
		#y el contexto, que en este caso es el formulario form mandado en un diccionario
		return render(request, 'mascota/mascota_form.html', {'form':form})

		#En el contexto la clave es form y va a contener el form que es el de 
		# la linea 19, es decir, form = MascotaForm(request.POST)


def mascota_list(request):
			#definimos nuestro queryset, al que le diremos que nos traiga todos los
			#objetos que están en nuestro modelo mascota.
			mascota = Mascota.objects.all().order_by('id')
			#A la variable contexto se le asigna el diccionario mascotas 
			#La clave de diccionario va a ser mascotas y va a ser igual a todo
			#lo que obtuvo en nuestro query set, osease Mascota.objects.all()
			contexto = {'mascotas':mascota}
			#retornamos un render, aqui mandamos el template, el nombre del template
			#y el contexto
			return render(request, 'mascota/mascota_list.html', contexto)


#Esta VISTA o funcion recibira un request y el id de mascota
def mascota_edit(request, id_mascota):		
	#Primero vamos a crear un Queryset el cual va a tener un objeto 
	#al que corresponde al id que estamos enviando
	mascota = Mascota.objects.get(id=id_mascota)
	#ahora mandamos los datos de este objeto a nuestro formulario.
	#Si el metodo es un GET lo que va a hacer es que nuestro formulario, 
	#lo va a rellenar con una instancia de el objeto que recogimos anteriormente.
	if request.method == 'GET':
		form = MascotaForm(instance=mascota)
	#Despues de recoger el POST del Formulario, lo instanciara
	#al objeto para guardar los cambios del objeto recogido 
	#de acuerdo a los parametros que estamos mandando.
	else:
		form = MascotaForm(request.POST, instance=mascota)
		#Aqui evaluamos si el formulario es valido
		if form.is_valid():
			#Y si es valido, guardará los cambios
			form.save()	
			#Después de realizar esto nos redirigirá a otra url
			#que podría ser por ejemplo el listado de mascotas
			return redirect('mascota:mascota_listar')
	#Luego retornamos el render y le ponemos el template que
	#usamos para guardar y como contexto le enviamos el formulario
	return render(request, 'mascota/mascota_form.html', {'form':form})


#Vista para eliminar registro de modelo Mascota
def mascota_delete(request, id_mascota):
	mascota = Mascota.objects.get(id=id_mascota)
	if request.method == 'POST':#Si el metodo es POST vamos a borrar el objeto
		mascota.delete()
		return redirect('mascota:mascota_listar')
	return render(request, 'mascota/mascota_delete.html', {'mascota':mascota})
	#Y retornamos el render, y lo mandaremos a un template
	#llamado mascota_delete y como contexto le mandamos
	#el objeto de la mascota


#Vistas basadas en clase.

#Creamos clase MascotaList que extiende de vista generica ListView
class MascotaList(ListView):
	#Le indicamos el modelo y le indicamos a que template enviaremos este contexto
	model = Mascota#.objects.all().order_by('id')
	template_name = 'mascota/mascota_list.html'
	paginate_by = 2 #cuantos objetos mandamos por pagina, en este caso solo muestra dos elementos por pagina

#Creamos clase MascotaCreate que extiende de vista generica CreateView
class MascotaCreate(CreateView):
	model = Mascota#modelo Mascota
	form_class = MascotaForm#formulario es MascotaForm
	template_name = 'mascota/mascota_form.html'#el template html
	#Una vez que guardemos nuestros registos, redirigimos a mascota_list
	success_url = reverse_lazy('mascota:mascota_listar')


	#Vista de clase Update
class MascotaUpdate(UpdateView):
	model = Mascota
	form_class = MascotaForm
	template_name = 'mascota/mascota_form.html'
	success_url = reverse_lazy('mascota:mascota_listar')

	#Vista de clase Delete
class MascotaDelete(DeleteView):
	model = Mascota
	template_name = 'mascota/mascota_delete.html'
	success_url = reverse_lazy('mascota:mascota_listar')