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

def home(request):
    # return render(request, 'home.html')
    return HttpResponse('<h1>hello</h1>')

def about_us(request):
    return render(request, 'about.html')

# @login_required
def drink_index(request):
    drinks = Drink.objects.all()
    return render(request, 'drinks/index.html', {'drinks': drinks})

###################### NEEDS ATTENTION ######################
# @login_required
def drinks_detail(request, drink_id):
    drink = Drink.objects.get(id=drink_id)
    # select name, description from table_name where
    # id = drink_id
    #i = drink.ingredients.all().values_list('id')
    #ingredients_drink_doesnt_have = Ingredient.objects.exclude(id_in=i)
    recipe_form = RecipeForm()
    return render(
        request,
        'drinks/detail.html',
        {'drink': drink, 'recipe_form': recipe_form, }
    )
    # code to link to recipes, referring to this code from catcollector:
    # toys_cat_doesnt_have = Toy.objects.exclude(id__in = cat.toys.all().values_list('id'))
<<<<<<< HEAD
    # i = drink.ingredients.all().values_list('id')
    # ingredients_pokemon_doesnt_have = Drink.objects.exclude(id_in=i)
    recipe_form =RecipeForm()
    return render(
        request,
        'drinks/detail.html',
        {'drink':drink, 'recipe_form': recipe_form,}
   )


# @login_required
def add_recipe(request, drink_id):
    form = RecipeForm(request.POST)
    if form.is_valid():
        new_recipe = form.save(commit=False)
        new_recipe.drink_id = drink_id
        new_recipe.save()
    return redirect('detail', drink_id=drink_id)

# class DrinkCreate(LoginRequiredMixin, CreateView):
class DrinkCreate(CreateView):
    model = Drink
    fields = ['name', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self, **kwargs):
        return reverse('detail', args=(self.object.id, ))

# do we want to give users the functionality to delete an entire drink complete with recipes?
class DrinkUpdate(UpdateView):
    model = Drink
    fields = ['name', 'description']

    def get_success_url(self, **kwargs):
        return reverse('detail', args=(self.object.id, ))


class DrinkUpdate(UpdateView):
    model = Drink
    fields = ['description', 'age']
    def get_success_url(self, **kwargs):
        return reverse('detail', args=(self.object.id, ))
        
###################### NEEDS ATTENTION ######################
class RecipeDetail(DetailView):
    def get(self, request):
        return HttpResponse('<h1>this is recipe detail</h1>')

###################### NEEDS ATTENTION ######################
class RecipeCreate(CreateView):
    def get(self, request):
        return HttpResponse('<h1>this is recipe create</h1>')

###################### NEEDS ATTENTION ######################
# class RecipeDelete(LoginRequiredMixin, DeleteView):
class RecipeDelete(DeleteView):
    # model = Recipe
    # success_url = 'drink detail (unsure how to link this just yet)'
    pass

###################### NEEDS ATTENTION ######################
# the below classes may take some fiddling. not sure if a function based view is best for recipes.
class IngredientList(ListView):
    model = Ingredient

class IngredientCreate(CreateView):
    model = Ingredient
    fields = '__all__'

class IngredientUpdate(UpdateView):
    model = Ingredient
    fields = ['type']

###################### NEEDS ATTENTION ######################
# refer to toys for this one in catcollector. this is to associate ingredients with recipes.
# this may be incorrect, please help review!
def assoc_ingredient(request, recipe_id, ingredient_id):
    Recipe.objects.get(id=recipe_id).ingredients.add(ingredient_id)
    return redirect('detail', recipe_id=recipe_id) # the detail here would be the drink detail.

# this is for AWS down the line.
def some_function(request):
    secret_key = os.environ['SECRET_KEY']




