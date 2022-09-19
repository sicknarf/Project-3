from django.db import models

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
        default = INGREDIENT_TYPE[0][0]
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

    def __str__(self):
        return self.name

class Recipe(models.Model):
    ingredients: models.ManyToManyField(Ingredient)
    skill_level = models.CharField(
        max_length = 1,
        choices = SKILL,
        default = SKILL[1][0]
    )
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)

    def __str__(self):
        # return f"a {len(self.ingredients)} ingredient recipe for {self.drink}"
        pass

class Photo(models.Model):
    url = models.CharField(max_length=200)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for drink_id:{self.drink_id} @{self.url}"