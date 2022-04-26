from dataclasses import field
from urllib import request, response
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import HttpResponseRedirect


from articulos.models import Articulos, Categoria
from articulos.forms import FromCategoria

class ListaCategorias(ListView):
    model = Categoria
    # queryset = Categoria.objects.order_by('nombre')
    paginate_by = 2

class NuevaCategoriaView(SuccessMessageMixin, CreateView):
    model = Categoria
    #fields = '__all__'
    form_class = FromCategoria
    success_url = reverse_lazy('categorias_lista') #redirecciona a la url
    extra_context = {'accion': 'Nueva'}
    success_message = 'Categoria %(nombre)s creada correctamente'

class EditarCategoriaView(SuccessMessageMixin, UpdateView):
    model = Categoria
    fields = '__all__'
    success_url = reverse_lazy('categorias_lista')
    extra_context = {'accion': 'Editar'}
    success_message = 'Categoria %(nombre)s modificada correctamente'
    

class EliminarCategoriaView(DeleteView):
    model = Categoria
    success_url = reverse_lazy('categorias_lista')

    def form_valid(self, form): # Call the delete() method on the fetched object and then redirect to the success URL.
        self.object = self.get_object() #trae el objeto
        if  Articulos.objects.filter(categoria=self.object):
            messages.error(self.request, 'No se puede elimiar la categoria, tiene articulos asociados.')
        else:
            self.object.delete()
            messages.error(self.request, 'Se elimino con exito la categoria.')
        return HttpResponseRedirect(self.success_url)

class BienvenidaView(SuccessMessageMixin,TemplateView):
    template_name = 'bienvenida.html'
    extra_context = {'mensaje': 'Bienvenid@ %(User.name)s'}
