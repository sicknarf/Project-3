from django.urls import path
from main_app import views

urlpatterns = [
    # http://localhost:8000
    path('', views.home, name='home'),
    # http://localhost:8000/about-us/
    path('about-us/', views.about_us, name='about_us'),
    # http://localhost:8000/drinks/
    path('drinks/', views.drink_index, name='index'),
    # http://localhost:8000/drinks/1/
    path('drinks/<int:drink_id>/', views.drinks_detail, name='detail'),
    # new route used to show a form and create a drink.
    # http://localhost:8000/drinks/create/
    path('drinks/create/', views.DrinkCreate.as_view(), name='drinks_create'),
    # http://localhost:8000/drinks/2/update/
    path('drinks/<int:pk>/update/',
         views.DrinkUpdate.as_view(), name='drinks_update'),
    # http://localhost:8000/drinks/2/delete/
    path('drinks/<int:pk>/delete/',
         views.DrinkDelete.as_view(), name='drinks_delete'),


    # http://localhost:8000/ingredients/
    path('ingredients/index/', views.IngredientList.as_view(), name='ingredients_index'),
    # http://localhost:8000/ingredients/edit
    path('ingredients/<int:pk>/update/', views.IngredientUpdate.as_view(), name="update_ingredient"),
    # http://localhost:8000/ingredients/delete
    # path('ingredients/<int:pk>/delete/', views.IngredientDelete.as_view(), name="delete_ingredient"),
    # http://localhost:8000/ingredients/detail
    path('ingredients/<int:ingredient_id>/', views.ingredient_detail, name='ingredient_detail'),
    path('ingredients/', views.add_ingredient, name="add_ingredient"),


    # http://localhost:8000/drinks/1/recipes/1/
    path('ingredients/<int:drink_id>/recipes/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    # http://localhost:8000/drinks/1/recipes/create/
    path('drinks/<int:drink_id>/recipes/create/', views.add_recipe, name='add_recipe'),
    # http://localhost:8000/drinks/1/recipes/1/delete/
    path('ingredients/<int:drink_id>/recipes/<int:pk>/delete', views.RecipeDelete.as_view(), name='recipe_delete'),
    # http://localhost:8000/drinks/1/recipes/1/edit/
    path('ingredients/<int:drink_id>/recipes/<int:pk>/edit', views.RecipeUpdate.as_view(), name='recipe_update'),
    

    path('accounts/signup/', views.signup, name='signup'),
]