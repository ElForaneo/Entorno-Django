from django.db import models

# Create your models here.

#Model de Autor
class Autor(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

#Modelos de los comentarios

class Comentario(models.Model):
    contenido = models.CharField(max_length=200)
    creacion_fecha = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.contenido

#Modelos de las publicaciones
class Publicacione(models.Model):
    titulo = models.CharField(max_length=40)
    contenido = models.CharField(max_length=250)
    creacion_fecha = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    reaccion = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo


