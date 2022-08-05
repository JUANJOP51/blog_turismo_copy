from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Articulo(models.Model):
    titulo = models.CharField(max_length=70)
    subtitulo = models.CharField(max_length=70)
    #usuario deberia ser una ForeingnKey que trae de BD de usuarios?? 
    autor = models.CharField(max_length=50)
    cuerpo = models.TextField(max_length=400)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    #vemos como hacemos la fecha de mod sino la sacamos
    fecha_mod = models.DateTimeField(auto_now=True)
    #chequear que este bien lo de la imagen:
    #imagen = models.ImageField(upload_to = 'media', null = True, blank = True)
    
    #fecha_string = fecha_mod.ToString("dd/MM/yyy")
    def __str__(request):
        return f'({request.titulo},{request.autor}, {request.fecha_mod.strftime("%Y/%m/%d-%H:%M:%S")})'

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
    
