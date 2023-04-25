from django.urls import path
from .import views

urlpatterns = [
    path('holi/', views.prueba, name="prueba_view"),
    path('show_inventory/<int:store_id>/', views.show_inventory, name="show_inventory_view"),
    path('show_store', views.show_store, name="show_store"),
    path('best_custom', views.best_custom, name="best_custom"),
    path('best_rent', views.best_rent, name="best_rent"),
    path('show_inventory/<int:store_id>/<int:film_id>/', views.show_inventory, name="show_inventory"),
    path('add_inventory/<int:store_id>/<int:film_id>/', views.add_inventory, name="add_inventory"),
    path('delete_inventory/<int:inventory_id>/', views.delete_inventory, name="delete_inventory"),
    path('update_inventory/<int:inventory_id>/<int:film_id>/', views.update_inventory, name="update_inventory"),
]