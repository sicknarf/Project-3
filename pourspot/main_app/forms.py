from django.forms import ModelForm
from django import forms
from .models import Ingredient, Recipe

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        # I am unsure about the below piece of code
        fields = ['ingredients', 'instructions', 'skill_level', 'drink']
        ingredients = forms.ModelMultipleChoiceField(
            queryset=Ingredient.objects.all(),
            widget=forms.CheckboxSelectMultiple,
        )