from django.contrib import admin
from .models import Actor, Language, Film, film_actor, Category, film_category

# Register your models here.
admin.site.register(Actor)
admin.site.register(Language)
admin.site.register(Film)
admin.site.register(film_actor)
admin.site.register(Category)
admin.site.register(film_category)