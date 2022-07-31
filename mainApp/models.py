from django.db import models
import datetime

# Create your models here.

class Articulo(models.Model):
    titulo = models.CharField(max_length=70)
    subtitulo = models.CharField(max_length=70)
    #usuario deberia ser una ForeingnKey que trae de BD de usuarios?? 
    autor = models.CharField(max_length=50)
    cuerpo = models.CharField(max_length=200)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    #vemos como hacemos la fecha de mod sino la sacamos
    fecha_mod = models.DateTimeField(auto_now=True)
    #chequear que este bien lo de la imagen:
    #imagen = models.ImageField(upload_to = 'media', null = True, blank = True)
    
    #fecha_string = fecha_mod.ToString("dd/MM/yyy")
    def __str__(request):
        return f'({request.titulo},{request.autor}, {request.fecha_mod.strftime("%Y/%m/%d-%H:%M:%S")})'
