from django.db import models
from datetime import date


# Create your models here.
class Actor(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    last_update = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'actor'

class Language(models.Model):
    name = models.CharField(max_length = 20)
    last_update = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'language'

class Film(models.Model):
    film_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 255)
    description = models.TextField()
    release_year = models.IntegerField()
    rental_duration = models.SmallIntegerField()
    rental_rate = models.DecimalField(max_digits=4, decimal_places=2)
    length = models.SmallIntegerField()
    replacement_cost = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.TextField()
    special_features = models.TextField(max_length = 100)
    language = models.ForeignKey('Language', models.DO_NOTHING)
    last_update = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'film'
    def __str__(self):
        return self.Film

class film_actor(models.Model):
    actor = models.OneToOneField(Actor, models.DO_NOTHING, primary_key=True)  # The composite primary key (actor_id, film_id) found, that is not supported. The first column is selected.
    film = models.ForeignKey(Film, models.DO_NOTHING)
    last_update = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'film_actor'
        unique_together = (('actor', 'film'),)

class Category(models.Model):
    name = models.CharField(max_length = 25)
    last_update = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'category'

class film_category(models.Model):
    film = models.OneToOneField(Film, models.DO_NOTHING, primary_key=True)  # The composite primary key (film_id, category_id) found, that is not supported. The first column is selected.
    category = models.ForeignKey(Category, models.DO_NOTHING)
    last_update = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'film_category'
        unique_together = (('film', 'category'),)