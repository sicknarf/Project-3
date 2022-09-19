from django.contrib import admin
from main_app.models import Drink, Ingredient, Recipe

# Register your models here.
admin.site.register(Drink)
admin.site.register(Recipe)
admin.site.register(Ingredient)