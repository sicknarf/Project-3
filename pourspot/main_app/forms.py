from django.forms import ModelForm
from django import forms
from .models import SKILL, Ingredient, Recipe, INGREDIENT_TYPE 

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'ingredients', 'instructions', 'skill_level']
        ingredients = forms.ModelChoiceField(
            Ingredient.objects.all(),
            )
        skill_level = forms.CharField(
            label='Choose the difficulty of this recipe', 
            widget=forms.Select(choices=SKILL),)

class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields =['name', 'type']

    type = forms.CharField(
        label='what type?',
        widget=forms.Select(choices=INGREDIENT_TYPE),
    )