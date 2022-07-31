from django import forms

class Articulo_form(forms.Form):
    titulo = forms.CharField()
    subtitulo = forms.CharField()
    #usuario deberia ser una ForeingnKey que trae de BD de usuarios?? 
    autor = forms.CharField()
    cuerpo = forms.CharField()
    #fecha_creacion = forms.DateTimeField()
    #vemos como hacemos la fecha de mod sino la sacamos
    #fecha_mod = forms.DateTimeField()
    #chequear que este bien lo de la imagen:
    #imagen = forms.ImageField(upload_to = 'media', null = True, blank = True)
