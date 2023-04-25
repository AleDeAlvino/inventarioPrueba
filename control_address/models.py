from django.db import models
from datetime import date

# Create your models here.
class Country(models.Model):
    country = models.CharField(max_length = 50, unique=True)
    last_update = models.DateTimeField(default = date.today)
    class Meta:
        managed = False
        db_table = 'country'

class City(models.Model):
    city = models.CharField(max_length = 50)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)
    last_update = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'city'

class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length = 50)
    address2 = models.CharField(max_length = 50, blank=True, null=True)
    phone = models.CharField(max_length = 20)
    postal_code = models.CharField(max_length = 10)
    district = models.CharField(max_length = 20)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    last_update = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'address'
    def __str__(self):
        return self.Address