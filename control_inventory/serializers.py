from .models import Store, Staff, Customer, Inventory, Rental, Payment
from rest_framework import serializers

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['store_id', 'manager_staff_id', 'address_id', 'last_update']


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['id', 'first_name', 'last_name' , 'email', 'active', 'username', 'password', 'picture', 'store_id', 'address_id', 'last_update']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name' , 'email', 'activebool', 'create_date', 'active', 'address_id', 'store_id', 'address_id', 'last_update']

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['inventory_id', 'film', 'store_id', 'last_update']

class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = ['id', 'rental_date', 'inventory_id' , 'customer_id', 'staff_id', 'return_date', 'last_update']

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'amount', 'customer_id' , 'staff_id', 'rental_id', 'payment_date']
