from django.forms import ModelForm
from django import forms
from .models import SKILL, Ingredient, Recipe, INGREDIENT_TYPE 

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        # I am unsure about the below piece of code
        fields = ['ingredients', 'instructions', 'skill_level']
        ingredients = forms.ModelChoiceField(Ingredient.objects.all())
        # ingredients = forms.ModelMultipleChoiceField(
        #     queryset=Ingredient.objects.all(),
        #     widget=forms.CheckboxSelectMultiple,
        # )
        skill_level = forms.CharField(
            label='What is your favorite fruit?', 
            widget=forms.Select(choices=SKILL),)

class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields =['name', 'type']

    type = forms.CharField(
        label='test',
        widget=forms.Select(choices=INGREDIENT_TYPE),

    )
