from django.db import models
from django.urls import reverse
#from datetime import date
# Import the User
from django.contrib.auth.models import User

SKILL = (
    ('B', 'Beginner'),
    ('I', 'Intermediate'),
    ('A', 'Advanced')
)

# I might have over-complicated this. let me know if this is acceptable, or otherwise not
INGREDIENT_TYPE = (
    ('S', 'Spirit'),
    ('R', 'Sour'),
    ('F', 'Fizz'),
    ('M', 'Smash'),
    ('P', 'Syrup'),
    ('B', 'Bitters'),
    ('H', 'Herb'),
    ('J', 'Juice'),
    ('G', 'Garnish'),
    ('O', 'Other')
)

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(
        max_length = 1,
        choices = INGREDIENT_TYPE,
    )
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('ingredients_detail', kwargs={'pk': self.id})
        pass


class Drink(models.Model):
    name = models.CharField(max_length=100)  # HAS A
    description = models.TextField(max_length=250)
    # is_private = models.BooleanField()
     # Add the foreign key linking to a user instance
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=30)
    ingredients = models.ManyToManyField(Ingredient)
    instructions = models.TextField(max_length=1000)
    skill_level = models.CharField(
        max_length = 1,
        choices = SKILL,
        default = SKILL[0][0]
    )
    
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.drink} recipe made with {self.ingredients}"

class Photo(models.Model):
    url = models.CharField(max_length=200)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for drink_id: {self.drink_id} @{self.url}"