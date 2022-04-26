from django.urls import path
from articulos import views, views_categoria


urlpatterns = [
    path('', views_categoria.BienvenidaView.as_view(), name='bienvenida'),
    path('articulos/', views.lista_articulos, name='articulos_lista'),
    path('articulos/nuevo', views.nuevo_articulo, name='nuevo_articulo'),
    path('articulos/eliminar/<int:id>', views.eliminar_articulos, name='eliminar_articulos'),
    path('articulos/editar/<int:id>', views.editar_articulos, name='editar_articulos'),
    path('listacategoria', views.lista_categoria, name='categoria_lista'),
    path('nuevacategoria', views.nueva_categoria, name='nueva_categoria'),
    path('eliminarcategoria/<int:id>', views.eliminar_categoria, name='eliminar_categoria'),
    path('editarcategoria/<int:id>', views.editar_categoria, name='editar_categoria'),

    path('categorias', views_categoria.ListaCategorias.as_view(), name='categorias_lista'),
    path('categorias/nueva', views_categoria.NuevaCategoriaView.as_view(), name='nueva_categorias'),
    path('categorias/editar/<int:pk>', views_categoria.EditarCategoriaView.as_view(), name='editar_categorias'),
    path('categorias/eliminar/<int:pk>', views_categoria.EliminarCategoriaView.as_view(), name='eliminar_categorias'),
]
