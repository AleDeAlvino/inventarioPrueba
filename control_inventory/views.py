from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Inventory, Rental
from control_address.models import Address
from control_films.models import Film
from .serializers import InventorySerializer, StoreSerializer
from control_address.serializers import AddressSerializer
from django.http import HttpResponseServerError
# from datetime import date
from django.utils import timezone
from django.db.models import Count

# Create your views here.

@api_view()
def prueba(request):
    
    return JsonResponse({"message": "Hello, world!"})

@api_view(['GET','POST'])
def add_inventory(request, store_id, film_id):

    try:
        film = Film.objects.filter(pk=film_id).first()
        Inventory.objects.create(film=film, store_id=store_id, last_update=timezone.now())
        return Response({"code": 200, "message": "Se agregó correctamente al inventario"})
    except Exception as e:
        return HttpResponseServerError("Ocurrió un error inesperado: " + str(e))
    

@api_view(['GET','POST'])
def delete_inventory(request, inventory_id):

    try:
        inventory = get_object_or_404(Inventory,pk=inventory_id)
        inventory.delete();
        return Response({"code": 200, "message": "Se elimino correctamente del inventario"})
    except Exception as e:
        return HttpResponseServerError("Ocurrió un error inesperado: " + str(e))
    

@api_view(['GET','POST'])
def update_inventory(request, inventory_id, film_id):

    try:
        inventory = Inventory.objects.filter(inventory_id = inventory_id).first()
        film = Film.objects.filter(pk=film_id).first()
        inventory.film = film;
        inventory.save();
        return Response({"code": 200, "message": "Se actualizo correctamente la pelicula"})
    except Exception as e:
        return HttpResponseServerError("Ocurrió un error inesperado: " + str(e))

@api_view()
def show_inventory(request, store_id, film_id):
    try:
        inventoryobj = Inventory.objects.filter(store_id = store_id, film = film_id).count()
        inventoryobj2 = Inventory.objects.filter(store_id = store_id, film = film_id)
        serializer = InventorySerializer(inventoryobj2, many=True)
        return Response({ "code": 200, "message": "Todo salio bien", "cont" : inventoryobj, "data": serializer.data})
    except Exception as e:
        return HttpResponseServerError("Ocurrió un error inesperado: " + str(e))

@api_view()
def show_store(request):
    try:
        storeobj = Address.objects.filter(store__isnull=False).distinct()
        serializer = AddressSerializer(storeobj, many=True)
        return Response({ "code": 200, "message": "Todo salio bien", "data" : serializer.data})
    except Exception as e:
        return HttpResponseServerError("Ocurrió un error inesperado: " + str(e))
    
@api_view()
def best_custom(request):
    try:
        # rental_counts = Rental.objects.values('customer_id').annotate(numero=Count('customer_id')).order_by('-numero')[:5]
        resultados = Rental.objects.values('customer_id', 'customer__first_name', 'customer__last_name').annotate(numero=Count('customer_id')).order_by('-numero')[:5]
        # serializer = AddressSerializer(rental_counts, many=True)
        print(resultados)
        return Response({ "code": 200, "message": "Todo salio bien", "data" : resultados})
    except Exception as e:
        return HttpResponseServerError("Ocurrió un error inesperado: " + str(e))

@api_view()
def best_rent(request):
    try:
        resultados = Rental.objects.values('inventory__film__title', 'inventory__film__film_id').annotate(numero=Count('inventory_id')).order_by('-numero')[:5]
        print(resultados)
        return Response({ "code": 200, "message": "Todo salio bien", "data" : resultados})
    except Exception as e:
        return HttpResponseServerError("Ocurrió un error inesperado: " + str(e))