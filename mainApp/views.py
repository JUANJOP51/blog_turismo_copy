from django.shortcuts import render
from django.http import HttpResponse
from mainApp.models import *
from mainApp.forms import Articulo_form
from django.views.generic import ListView

# Create your views here.

def index(request):
    return render(request, "mainApp/index.html")

def about(request):
    return render(request, "mainApp/about.html")

def pages(request):
    return render(request, "mainApp/pages.html")

#crear articulo en el blog (Crud)

def crear_art(request):

    if request.method == 'POST': #VER COMO AGREGAR AUTOR QUE SE SACARIA DEL QUE ESTA LOGUEADO, FECHA CON GETDATE? y recibir imagen

        formulario = Articulo_form(request.POST)
        print(formulario)

        if formulario.is_valid:
            info = formulario.cleaned_data
            articulo = Articulo(titulo=info['titulo'], subtitulo=info['subtitulo'], autor=info['autor'], cuerpo=info['cuerpo'],fecha_creacion=info['fecha_creacion'], fecha_mod=info['fecha_mod'], imagen=info['imagen'])
            
            articulo.save()

            #VER DE QUE MANDE O MUESTRE UN MENSAJE QUE LA PUBLICACION SE CREO CON EXITO
            return render(request, "mainApp/index.html")
    else:

        formulario = Articulo_form()

    return render(request, "mainApp/crear_articulo.html", {"formulario":formulario})

#listar articulos del blog (cRud)
"""
def listar_art(request):

    articulos = Articulo.objects.all()

    contexto = {"articulos":articulos}

    return render(request, "mainApp/pages.html", contexto)
"""

#CRUD con ListView clases basadas en vistas // listar articulos del blog

class articulo_list(ListView):

    model = Articulo
    template = "mainApp/pages.html"

#eliminar articulo del blog (cruD)

def eliminar_art(request, pagina):

    articulo = Articulo.objects.get(titulo=pagina)
    articulo.delete()

    articulos = Articulo.objects.all()

    contexto = {"articulos":articulos}

    return render(request, "mainApp/pages.html", contexto)

#editar articulo del blog (crUd)

def editar_art(request, pagina):
    
    articulo = Articulo.objects.get(titulo=pagina)

    if request.method == 'POST': #VER COMO AGREGAR AUTOR QUE SE SACARIA DEL QUE ESTA LOGUEADO, FECHA CON GETDATE? y recibir imagen

        formulario = Articulo_form(request.POST)
        print(formulario)

        if formulario.is_valid:

            info = formulario.cleaned_data

            articulo = Articulo(titulo=info['titulo'], subtitulo=info['subtitulo'], autor=info['autor'], cuerpo=info['cuerpo'],fecha_creacion=info['fecha_creacion'], fecha_mod=info['fecha_mod'], imagen=info['imagen'])
            
            articulo.save()

            #VER DE QUE MANDE O MUESTRE UN MENSAJE QUE LA PUBLICACION SE CREO CON EXITO
            return render(request, "mainApp/index.html")
    else:

        formulario = Articulo_form(initial={'titulo': articulo.titulo,'subtitulo':articulo.subtitulo, 'autor':articulo.autor, 'cuerpo':articulo.cuerpo, 'fecha_creacion':articulo.fecha_creacion, 'fecha_mod':articulo.fecha_mod})

    return render(request, "mainApp/modificar_articulo.html", {"formulario":formulario, 'pagina':pagina})

