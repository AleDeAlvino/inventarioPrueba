from django.urls import path
from .import views

urlpatterns = [
    path('show_film', views.show_film, name="show_film"),
]