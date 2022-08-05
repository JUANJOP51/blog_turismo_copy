from django.urls import path
from mainApp import views

urlpatterns = [
    path('', views.index),
    path('index/', views.index),
    path('about/', views.about, name="about"),
    #path('pages', views.listar_art, name="paginas"),
    path('crear_articulo/', views.crear_art, name="crear_articulo"),
    path('borrar_articulo/<pagina>/', views.eliminar_art, name="eliminar_articulo"),
    path('modificar_articulo/<pagina>/', views.editar_art, name="editar_articulo"),
    path('pages/', views.articulo_list.as_view(), name='list'),
    path('editarPerfil/', views.editarPerfil, name='editarPerfil'),
    path('agregarAvatar/', views.agregarAvatar, name='agregarAvatar'),


    #al mensaje lo hago desde aca o desde la app messageApp?
    #path('messageApp/messages', views.mensaje, name="mensaje"),
]
"""
completar las views."FUNCION" como corresponda
path('about', views., name=""),
path('articulos', views., name=""),
path('borrar_articulo', views., name=""),
path('crear_articulo', views., name=""),
"""