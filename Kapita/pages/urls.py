#pages/urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('', home.as_view(), name="home"),
    path('Publicaciones/Add', Publicacionesadd.as_view(), name="pub_add"),
    path('Publicaciones/<int:id>/', PublicacionesUpdate.as_view(), name="pub_update")
    ]
