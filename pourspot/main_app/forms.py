from django.forms import ModelForm
from .models import Recipe

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        # I am unsure about the below piece of code
        fields = '__all__'