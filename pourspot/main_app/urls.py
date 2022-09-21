from django.urls import path
from main_app import viewsingredients
from . import views, viewsdrinks, viewsrecipe, viewsingredients

urlpatterns = [
    # http://localhost:8000
    path('', views.home, name='home'),
    # http://localhost:8000/about-us/
    path('about-us/', views.about_us, name='about_us'),
    # http://localhost:8000/drinks/
    path('drinks/', viewsdrinks.drink_index, name='index'),
    # http://localhost:8000/drinks/1/
    path('drinks/<int:drink_id>/', viewsdrinks.drinks_detail, name='detail'),
    # new route used to show a form and create a drink.
    # http://localhost:8000/drinks/create/
    path('drinks/create/', viewsdrinks.DrinkCreate.as_view(), name='drinks_create'),
    # http://localhost:8000/drinks/2/update/
    path('drinks/<int:pk>/update/',
         viewsdrinks.DrinkUpdate.as_view(), name='drinks_update'),
    # http://localhost:8000/drinks/2/delete/
    path('drinks/<int:pk>/delete/',
         viewsdrinks.DrinkDelete.as_view(), name='drinks_delete'),

    # http://localhost:8000/drinks/2/add_feeding/
    path('drinks/<int:drink_id>/add_recipe/', viewsrecipe.add_recipe, name="add_recipe"),

    # these links needs to be formatted so it takes us to recipes & ingredients
    # path('drinks/<int:drink>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
    # path('drinks/<int:drink>/add_photo', views.add_photo, name='add_photo'),

    # http://localhost:8000/ingredients/
    path('ingredients/index/', viewsingredients.IngredientList.as_view(), name='ingredients_index'),
    # http://localhost:8000/ingredients/detail
    path('ingredients/<int:ingredient_id>/', viewsingredients.ingredient_detail, name='ingredient_detail'),
    # path('ingredients/', viewsingredients.IngredientCreate.as_view(), name='ingredients_create'),
    path('ingredients/', viewsingredients.add_ingredient, name="add_ingredient"),
    # http://localhost:8000/ingredients/edit
    path('ingredients/<int:pk>/update/', viewsingredients.IngredientUpdate.as_view(), name="update_ingredient"),
    # http://localhost:8000/ingredients/delete
    path('ingredients/<int:pk>/delete/', viewsingredients.IngredientDelete.as_view(), name="delete_ingredient"),
    # http://localhost:8000/drinks/1/recipes/1/
    ###################### NEEDS ATTENTION ######################
    # this was previously <int:pk> instead of <int:drink_id> and <int:recipe_id>
    path('ingredients/<int:drink_id>/recipes/<int:recipe_id>/', viewsrecipe.recipe_detail, name='recipe_detail'),

    ###################### NEEDS ATTENTION ######################
    # http://localhost:8000/drinks/1/recipes/create/
    # path('drinks/<int:drink_id>/recipes/create/', viewsrecipe.RecipeCreate.as_view(), name='recipe_create'),
    path('drinks/<int:drink_id>/recipes/create/', viewsrecipe.add_recipe, name='add_recipe'),

    ###################### NEEDS ATTENTION ######################
    # http://localhost:8000/drinks/1/recipes/1/delete/
    path('ingredients/<int:drink_id>/recipes/<int:pk>/delete', viewsrecipe.RecipeDelete.as_view(), name='recipe_delete'),
    path('ingredients/<int:drink_id>/recipes/<int:pk>/edit', viewsrecipe.RecipeUpdate.as_view(), name='recipe_update'),
    
    path('accounts/signup/', views.signup, name='signup'),
]