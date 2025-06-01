from meal_planner.database.setup import session
from meal_planner.models.recipe import Recipe
from meal_planner.models.ingredient import Ingredient


def get_or_create_ingredient(name, quantity):
    ingredient = session.query(Ingredient).filter_by(name=name).first()
    if ingredient:
        return ingredient
    ingredient = Ingredient(name=name, quantity=quantity)
    session.add(ingredient)
    return ingredient


def get_or_create_recipe(name, ingredients):
    recipe = session.query(Recipe).filter_by(name=name).first()
    if recipe:
        return recipe
    recipe = Recipe(name=name)
    recipe.ingredients = ingredients
    session.add(recipe)
    return recipe


def seed_sample_data():
    print("Seeding sample recipes and ingredients...")

    # Ingredients (with get_or_create logic)
    rice = get_or_create_ingredient("Rice", 200)
    chicken = get_or_create_ingredient("Chicken Breast", 300)
    broccoli = get_or_create_ingredient("Broccoli", 150)
    eggs = get_or_create_ingredient("Eggs", 2)
    tomato = get_or_create_ingredient("Tomato", 100)
    pasta = get_or_create_ingredient("Pasta", 250)
    cheese = get_or_create_ingredient("Cheese", 100)

    # Recipes
    get_or_create_recipe("Chicken Rice Bowl", [rice, chicken, broccoli])
    get_or_create_recipe("Tomato Pasta", [pasta, tomato, cheese])
    get_or_create_recipe("Veggie Omelette", [eggs, tomato, broccoli])

    session.commit()
    print("Seeding completed!")
