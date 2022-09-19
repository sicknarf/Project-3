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
def add_recipe(request, drink_id):
    form = RecipeForm(request.POST)
    if form.is_valid():
        new_recipe = form.save(commit=False)
        new_recipe.drink_id = drink_id
        new_recipe.save()
    return redirect('detail', drink_id=drink_id)


###################### NEEDS ATTENTION ######################
class RecipeDetail(DetailView):
    def get(self, request):
        return HttpResponse('<h1>this is recipe detail</h1>')

###################### NEEDS ATTENTION ######################
class RecipeCreate(CreateView):
    model = Recipe

###################### NEEDS ATTENTION ######################
# class RecipeDelete(LoginRequiredMixin, DeleteView):
class RecipeDelete(DeleteView):
    # model = Recipe
    # success_url = 'drink detail (unsure how to link this just yet)'
    pass
