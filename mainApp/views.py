from django.shortcuts import render
from django.http import HttpResponse
import mainApp
from mainApp.models import *
from mainApp.forms import Articulo_form, UserEditForm, UserCreationForm, UserRegisterForm, AvatarForm
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

def editarPerfil(request):
    usuario=request.user

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            usuario.email = informacion ['email']
            usuario.password1 = informacion ['password1']
            usuario.password2 = informacion ['password2']
            usuario.save()

            return render(request, 'mainApp/inicio.html')
    else:
        miFormulario = UserEditForm(initial={'email': usuario.email})
    
    return render(request, 'mainApp/editarPerfil.html', {'miFormulario': miFormulario, 'usuario': usuario.username})

def agregarAvatar(request):
    if request == 'POST':
        formulario = AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            AvatarViejo = Avatar.objects.get(user=request.user)
            if (AvatarViejo.avatar):
                AvatarViejo.delete()
            avatar=Avatar(user=request.user, imagen=formulario.cleaned_data ['imagen'])
            avatar.save
    else:
        formulario = AvatarForm()
    return render(request, 'mainApp/agregarAvatar.html', {'formulario': formulario, 'usuario':request.user})


