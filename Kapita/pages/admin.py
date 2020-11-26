from django.contrib import admin
from .models import Autor, Publicacione, Comentario

# Register your models here.

admin.site.register(Autor)
admin.site.register(Publicacione)
admin.site.register(Comentario)