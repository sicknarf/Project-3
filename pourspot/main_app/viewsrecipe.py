# imports for image uplaoading to AWS
import os
# import boto3
import uuid

# django imports
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required # for function based views
from django.contrib.auth.mixins import LoginRequiredMixin # for class based views
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.http import HttpResponse
from .models import Ingredient, Drink, Recipe
from .forms import RecipeForm
from enum import Enum



# @login_required
def add_recipe(request, drink_id):
    form = RecipeForm(request.POST)
    print(request.POST)
    if form.is_valid():
        new_recipe = form.save(commit=False)
        new_recipe.drink_id = drink_id
        new_recipe.save()
        form.save_m2m()
        drink = Drink.objects.get(id=drink_id)
        return render(request, 'drinks/detail.html', {'drink': drink})
    return render(request, 'main_app/recipe_form.html', {'form': form})

def recipe_detail(request, drink_id, recipe_id):
    drink = Drink.objects.get(id=drink_id)
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'drinks/recipe_detail.html', {'drink':drink, 'recipe':recipe})



# class RecipeDelete(LoginRequiredMixin, DeleteView):
class RecipeDelete(DeleteView):
    model = Recipe
    success_url = '/drinks/'

class RecipeUpdate(UpdateView):
    model = Recipe

    fields = ['instructions', 'ingredients', 'skill_level']
    def get_success_url(self, **kwargs):
        return reverse('recipe_detail', args=(self.object.drink.id, self.object.id, ))