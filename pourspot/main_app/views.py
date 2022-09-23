# imports for image uplaoading to AWS
import os
import boto3
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
from .models import Ingredient, Drink, Recipe, Photo
from .forms import RecipeForm, IngredientForm

def home(request):
    return render(request, 'home.html')

def about_us(request):
    return render(request, 'about.html')

def drink_index(request):
    drinks = Drink.objects.all()
    return render(request, 'drinks/index.html', {'drinks': drinks})

def drinks_detail(request, drink_id):
    drink = Drink.objects.get(id=drink_id)
    recipe_form = RecipeForm()
    return render(
        request,
        'drinks/detail.html',
        {'drink': drink, 'recipe_form': recipe_form }
    )

class DrinkCreate(LoginRequiredMixin, CreateView):
    model = Drink
    fields = ['name', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self, **kwargs):
        return reverse('detail', args=(self.object.id, ))

class DrinkUpdate(LoginRequiredMixin, UpdateView):
    model = Drink
    fields = ['name', 'description', ]
    def get_success_url(self, **kwargs):
        return reverse('detail', args=(self.object.id, ))

class DrinkDelete(LoginRequiredMixin, DeleteView):
    model = Drink
    success_url = '/drinks/'

class IngredientList(ListView):
    model = Ingredient
    fields = '__all__'

@login_required
def add_ingredient(request):
    ingredients = Ingredient.objects.all
    form = IngredientForm(request.POST)
    if form.is_valid():
        new_ingredient = form.save()
        new_ingredient.save()
    return render(request, 'main_app/ingredient_form.html', {'form': form, 'ingredients': ingredients})

def ingredient_detail(request, ingredient_id):
    ingredient = Ingredient.objects.get(id=ingredient_id)
    # return HttpResponse("test")
    ingredient_form=IngredientForm()
    return render(
        request, 
        'ingredients/ingredient_detail.html', 
        {'ingredient':ingredient,'ingredient_form': ingredient_form}
        )

class IngredientCreate(LoginRequiredMixin, CreateView):
    model = Ingredient
    fields = ['name','type']


class IngredientUpdate(LoginRequiredMixin, UpdateView):
    model = Ingredient

    fields = ['name', 'type' ]
    def get_success_url(self, **kwargs):
        return reverse('ingredient_detail', args=(self.object.id, ))

# commented out and removed this functionality to reduce interference with recipe m2m relationship
# leaving in for future implementation/improvement
# class IngredientDelete(LoginRequiredMixin, DeleteView):
#     model = Ingredient
#     success_url ='/ingredients/'

@login_required
def add_recipe(request, drink_id):
    form = RecipeForm(request.POST)
    print(request.POST)
    drink = Drink.objects.get(id=drink_id)
    if form.is_valid():
        new_recipe = form.save(commit=False)
        new_recipe.drink_id = drink_id
        new_recipe.save()
        form.save_m2m()
        drink = Drink.objects.get(id=drink_id)
        return render(request, 'drinks/detail.html', {'drink': drink})
    return render(request, 'main_app/recipe_form.html', {'form': form, 'drink':drink})

def recipe_detail(request, drink_id, recipe_id):
    drink = Drink.objects.get(id=drink_id)
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'drinks/recipe_detail.html', {'drink':drink, 'recipe':recipe})

class RecipeDelete(LoginRequiredMixin, DeleteView):
    model = Recipe
    success_url = '/drinks/'

class RecipeUpdate(LoginRequiredMixin, UpdateView):
    model = Recipe

    fields = ['instructions', 'ingredients', 'skill_level']
    def get_success_url(self, **kwargs):
        return reverse('recipe_detail', args=(self.object.drink.id, self.object.id, ))

# this is for AWS down the line.
def some_function(request):
    secret_key = os.environ['SECRET_KEY']

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid signup. Please try again.'

    form = UserCreationForm()
    context = {
        'form': form,
        'error_message': error_message
    }
    return render(request, 'registration/signup.html', context)

def add_photo(request, drink_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, drink_id=drink_id)
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail',drink_id=drink_id)    