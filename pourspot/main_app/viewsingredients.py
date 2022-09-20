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
from .forms import RecipeForm , IngredientForm



###################### NEEDS ATTENTION ######################
# the below classes may take some fiddling. not sure if a function based view is best for recipes.
class IngredientList(ListView):
    model = Ingredient
    fields = '__all__'

def add_ingredient(request):
    ingredients = Ingredient.objects.all
    form = IngredientForm(request.POST)
    if form.is_valid():
        new_ingredient = form.save()
        new_ingredient.save()
    return render(request, 'main_app/ingredient_form.html', {'form': form, 'ingredients': ingredients})

# class IngredientCreate(CreateView):
#     model = Ingredient
#     fields = ['name', 'type']

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)

def ingredient_detail(request, ingredient_id):
    ingredient = Ingredient.objects.get(id=ingredient_id)
    # return HttpResponse("test")
    ingredient_form=IngredientForm()
    return render(
        request, 
        'main_app/ingredient_detail.html', 
        {'ingredient':ingredient,'ingredient_form': ingredient_form}
        )

class IngredientUpdate(UpdateView):
    model = Ingredient
     # return HttpResponse("test")
    # fields = ['name','type']

    fields = ['name', 'type' ]
    def get_success_url(self, **kwargs):
        return reverse('ingredient_detail', args=(self.object.id, ))

    fields = ['name', 'type', ]
    def get_success_url(self, **kwargs):
        return reverse('ingredient_detail', args=(self.object.id, ))

class IngredientDelete(DeleteView):
    model = Ingredient
    success_url ='/ingredients/'

###################### NEEDS ATTENTION ######################
# refer to toys for this one in catcollector. this is to associate ingredients with recipes.
# this may be incorrect, please help review!
def assoc_ingredient(request, recipe_id, ingredient_id):
    Recipe.objects.get(id=recipe_id).ingredients.add(ingredient_id)
    return redirect('detail', recipe_id=recipe_id) # the detail here would be the drink detail.