from .models import Actor, Language, Film, film_actor, Category, film_category
from rest_framework import serializers

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'first_name', 'last_name', 'last_update']

class LenguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['lenguaje_id', 'name', 'last_update']

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['film_id', 'title', 'description', 'release_year', 'rental_duration', 'rental_rate', 'length', 'replacement_cost', 'rating', 'special_features', 'language', 'last_update']

class film_actorSerializer(serializers.ModelSerializer):
    class Meta:
        model = film_actor
        fields = ['id', 'actor_id', 'film_id', 'last_update']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'last_update']

class film_categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = film_category
        fields = ['id', 'film_id', 'category_id', 'last_update']
