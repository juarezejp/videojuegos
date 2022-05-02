from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from articulos.models import Articulos, Categoria
from articulos.forms import FromArticulo, FromCategoria
import logging

logger = logging.getLogger(__name__)

#Categorias
# URLConf->MVT
def lista_articulos(request):
    articulosl = Articulos.objects.all()
    #select * from articulos_articulos;
    paginator = Paginator(articulosl, 2) # Show 2 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'articulos.html', {'page_obj': page_obj})


    #paginator = Paginator(contact_list, 25) # Show 25 contacts per page.

    #page_number = request.GET.get('page')
    #page_obj = paginator.get_page(page_number)
    #return render(request, 'list.html', {'page_obj': page_obj})

def eliminar_articulos(request, id):
    Articulos.objects.get(id=id).delete()
    messages.error(request, 'Se elimino un articulo.')
    return redirect('articulos_lista')

def nuevo_articulo(request):
    if request.method == 'POST':#viene por post
        form = FromArticulo(request.POST)
        if form.is_valid():
            form.save()
            messages.error(request, 'Se agrego un nuevo articulo.')
            return redirect('articulos_lista')
    else:#viene por get
        form = FromArticulo()
        return render(request, 'nuevo_articulo.html',  {'form':form})

def editar_articulos(request, id):
    articulo = Articulos.objects.get(id=id) 
    if request.method == 'POST':#viene por post
        form = FromArticulo(request.POST, instance=articulo)
        if form.is_valid():
            form.save()
            messages.error(request, 'Se modifico un articulo.')
            return redirect('articulos_lista')
    else:#viene por get
        form = FromArticulo(instance=articulo)
        return render(request, 'nuevo_articulo.html',  {'form':form})

#Categorias
def lista_categoria(request):
    categorias = Categoria.objects.all()
    return render(request, 'categoriatemplates/categorias.html', {'categorias':categorias})

def nueva_categoria(request):
    if request.method == 'POST':#viene por post
        form = FromCategoria(request.POST)
        if form.is_valid():
            form.save()
            messages.error(request, 'Se agrego nueva categoria.')
            return redirect('categoria_lista')
    else:#viene por get
        form = FromCategoria()
        return render(request, 'categoriatemplates/nueva_categoria.html',  {'form':form})

def eliminar_categoria(request, id):
    #Categoria.objects.get(id=id).delete()
    #messages.error(request, 'Se elimino una categoria.')
    categoria_eliminar = Categoria.objects.get(id=id)
    if  Articulos.objects.filter(categoria=categoria_eliminar):
            messages.error(request, 'No se puede elimiar la categoria, tiene articulos asociados.')
    else:
        categoria_eliminar.delete()
        messages.error(request, 'Se elimino con exito la categoria.')
    return redirect('categoria_lista')

def editar_categoria(request, id):
    categoria = Categoria.objects.get(id=id) 
    if request.method == 'POST':#viene por post
        form = FromCategoria(request.POST, instance=categoria)
        logger.debug("ID de la categoria: "+categoria.id)
        if form.is_valid():
            form.save()
            logger.warning("Se modifico una categoria con exito")
            messages.error(request, 'Se modifico una categoria.')
            return redirect('categoria_lista')
    else:#viene por get
        form = FromCategoria(instance=categoria)
        return render(request, 'categoriatemplates/editar_categoria.html',  {'form':form})
