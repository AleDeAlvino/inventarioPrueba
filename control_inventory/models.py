from django.db import models
from control_address.models import Address
from control_films.models import Film


class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    email = models.CharField(max_length = 50)
    active = models.BooleanField(default=True)
    username = models.CharField(max_length = 16, unique=True)
    password = models.CharField(max_length = 40)
    picture = models.BinaryField(blank=True, null=True)
    store_id = models.SmallIntegerField()
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    last_update = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'staff'
    def __str__(self):
        return self.Staff

# Create your models here.
class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    manager_staff = models.OneToOneField(Staff, models.DO_NOTHING)
    address = models.ForeignKey(Address, models.DO_NOTHING)
    last_update = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'store'
    def __str__(self):
        return self.Store

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    store_id = models.SmallIntegerField()
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    email = models.CharField(max_length = 50)
    activebool = models.BooleanField(default=True)
    create_date = models.DateField()
    active = models.CharField(max_length = 100)
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    last_update = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'customer'
    def __str__(self):
        return self.Customer

class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    film = models.ForeignKey(Film, models.DO_NOTHING)
    store_id = models.SmallIntegerField()
    last_update = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'inventory'
    def __str__(self):
        return self.Inventory

class Rental(models.Model):
    rental_id = models.AutoField(primary_key=True)
    rental_date = models.DateTimeField()
    inventory = models.ForeignKey(Inventory, models.DO_NOTHING)
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    return_date = models.DateTimeField()
    last_update = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'rental'
        unique_together = (('rental_date', 'inventory', 'customer'),)
    def __str__(self):
        return self.Rental


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    amount = models.IntegerField()
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    staff_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    rental_id = models.ForeignKey(Rental, on_delete=models.CASCADE)
    payment_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'payment'
    def __str__(self):
        return self.Payment