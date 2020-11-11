#pages/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePageView, name="home"),
    path('Comments', views.CommentsView, name="Comments"),
    path('About', views.AboutView, name="About")
    ]
