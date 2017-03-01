from django.shortcuts import render
from django.http import HttpResponseRedirect
#importamos el resolver_lazy
from django.core.urlresolvers import reverse_lazy

#importamos las vistas genericas necesarias
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

#importamos los modelos a usar
from apps.adopciones.models import Persona, Solicitud

#importamos los formularios
from apps.adopciones.forms import PersonaForm, SolicitudForm


# Create your views here.

def index_adopcion(request):
	return HttpResponse("Soy la pagina principal de la app adopcion")

#Vistas basadas en Clases

#Listado
class SolicitudList(ListView):
	model = Solicitud
	template_name = 'adopcion/solicitud_list.html' 

#Crear
class SolicitudCreate(CreateView):
	model = Solicitud
	template_name = 'adopcion/solicitud_form.html'
	form_class =  SolicitudForm
	second_form_class = PersonaForm
	success_url = reverse_lazy('adopciones:solicitud_listar')#revisar aqui si es adopciones

	#sobreescribiremos el metodo get_context_data
	def get_context_data(self, **kwargs):
		context = super(SolicitudCreate, self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		if 'form2' not in context:
			context['form2'] = self.second_form_class(self.request.GET)
		return context
		
	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		form2 = self.second_form_class(request.POST)
		if form.is_valid() and form2.is_valid():
			solicitud = form.save(commit=False)
			solicitud.persona = form2.save()
			solicitud.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form, form2=form2))
			
#Lo que hacemos es recoger los valores que se ingresaron en los formularios, 
#verificamos si son validos, guardamos el primer form, se lo asignamos a solicitud
#Despues creamos la relacion y guardamos los valores del segundo form solicitud.persona = form2.save,  			
#y por ultimo guardamos el objeto.
#Si no es valido devolvemos el contexto, con formularios en blanco usando el
#self.render_to_response(self.get_context_data(form=form, form2=form2))		

#Actualizar
class SolicitudUpdate(UpdateView):
	model = Solicitud
	second_model = Persona
	template_name = 'adopcion/solicitud_form.html'
	form_class = SolicitudForm
	second_form_class = PersonaForm
	success_url = reverse_lazy('adopciones:solicitud_listar')

	#recogemos nuestros objetos
	def get_context_data(self, **kwargs):
		context = super(SolicitudUpdate, self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk', 0)
		solicitud = self.model.objects.get(id=pk) #el model es Solicitud
		persona = self.second_model.objects.get(id=solicitud.persona_id) #el second_model es Persona
		if 'form' not in context:#validamos que nuestros formularios esten en el contexto
			context['form'] = self.form_class()#asignamos el contexto
		if 'form2' not in context:
			context['form2'] = self.second_form_class(instance=persona)
		context['id'] = pk		
		return context

	#Sobreescribimos el metodo post
	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		id_solicitud = kwargs['pk']
		solicitud = self.model.objects.get(id=id_solicitud)
		persona = self.second_model.objects.get(id=solicitud.persona_id)
		form = self.form_class(request.POST, instance=solicitud)
		form2 = self.second_form_class(request.POST, instance=persona)
		if form.is_valid() and form2.is_valid():#validar los formularios, si son validos se guardan
			form.save()
			form2.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return HttpResponseRedirect(self.get_success_url())


#Eliminar
class SolicitudDelete(DeleteView):
	model = Solicitud
	template_name = 'adopcion/solicitud_delete.html'
	success_url = reverse_lazy('adopciones:solicitud_listar')			
