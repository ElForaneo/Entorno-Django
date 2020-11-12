#pages/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.commentsView, name="comments"),
    ]
