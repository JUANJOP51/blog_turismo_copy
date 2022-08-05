from django.contrib import admin
from .models import *
from .models import Comment
# Register your models here.

# Aca van los models que quiero administrar en admin
admin.site.register(Articulo)
admin.site.register(Avatar)

