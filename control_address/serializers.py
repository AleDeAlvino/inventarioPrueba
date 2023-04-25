from .models import Country, City, Address
from rest_framework import serializers

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_id', 'country', 'last_update']

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['city_id', 'city', 'country_id', 'last_update']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['address_id', 'address', 'address2', 'phone', 'postal_code', 'district', 'city_id', 'last_update']
