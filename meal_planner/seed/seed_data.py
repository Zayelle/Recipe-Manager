from meal_planner.database import SessionLocal, init_db
from meal_planner.models.recipe import Recipe
from meal_planner.models.ingredient import Ingredient
from meal_planner.models.meal_plan import MealPlan
from meal_planner.models.recipe_ingredient import RecipeIngredient

def get_or_create_ingredient(session, name):
    ingredient = session.query(Ingredient).filter_by(name=name).first()
    if ingredient:
        print(f"✔ Ingredient exists: {name}")
        return ingredient
    ingredient = Ingredient(name=name)
    session.add(ingredient)
    print(f"➕ Added new ingredient: {name}")
    return ingredient

def get_or_create_recipe(session, name):
    recipe = session.query(Recipe).filter_by(name=name).first()
    if recipe:
        print(f"✔ Recipe exists: {name}")
        return recipe
    recipe = Recipe(name=name)
    session.add(recipe)
    print(f"➕ Added new recipe: {name}")
    return recipe

def seed_sample_data(session):
    print("🌱 Seeding sample recipes and ingredients...")

    try:
        # Clear existing data (for development reset)
        session.query(RecipeIngredient).delete()
        session.query(MealPlan).delete()
        session.commit()

        with session.no_autoflush:

        # Ingredients
         rice = get_or_create_ingredient(session, "Rice")
         chicken = get_or_create_ingredient(session, "Chicken Breast")
         broccoli = get_or_create_ingredient(session, "Broccoli")
         eggs = get_or_create_ingredient(session, "Eggs")
         tomato = get_or_create_ingredient(session, "Tomato")
         pasta = get_or_create_ingredient(session, "Pasta")
         cheese = get_or_create_ingredient(session, "Cheese")

        # Recipes
        rice_bowl = get_or_create_recipe(session, "Chicken Rice Bowl")
        tomato_pasta = get_or_create_recipe(session, "Tomato Pasta")
        omelette = get_or_create_recipe(session, "Veggie Omelette")

        # Clear old relationships if they exist
        rice_bowl.recipe_ingredients = []
        tomato_pasta.recipe_ingredients = []
        omelette.recipe_ingredients = []

        # Associate recipe ingredients
        rice_bowl.recipe_ingredients = [
            RecipeIngredient(recipe=rice_bowl, ingredient=rice, quantity=200.0),
            RecipeIngredient(recipe=rice_bowl, ingredient=chicken, quantity=300.0),
            RecipeIngredient(recipe=rice_bowl, ingredient=broccoli, quantity=150.0),
        ]
        tomato_pasta.recipe_ingredients = [
            RecipeIngredient(recipe=tomato_pasta, ingredient=pasta, quantity=250.0),
            RecipeIngredient(recipe=tomato_pasta, ingredient=tomato, quantity=100.0),
            RecipeIngredient(recipe=tomato_pasta, ingredient=cheese, quantity=100.0),
        ]
        omelette.recipe_ingredients = [
            RecipeIngredient(recipe=omelette, ingredient=eggs, quantity=2.0),
            RecipeIngredient(recipe=omelette, ingredient=tomato, quantity=100.0),
            RecipeIngredient(recipe=omelette, ingredient=broccoli, quantity=150.0),
        ]

        # Add all recipes (they cascade recipe_ingredients if relationships are configured correctly)
        session.add_all([rice_bowl, tomato_pasta, omelette])

        # Meal Plans
        for day, recipe in [
            ("Monday", rice_bowl),
            ("Tuesday", tomato_pasta),
            ("Wednesday", omelette),
            ("Thursday", rice_bowl),
            ("Friday", tomato_pasta),
            ("Saturday", omelette),
            ("Sunday", rice_bowl),
        ]:
            session.add(MealPlan(day=day, recipe=recipe))

        session.commit()
        print(f"✅ Seeded {session.query(Recipe).count()} recipes, {session.query(Ingredient).count()} ingredients.")
    except Exception as e:
        session.rollback()
        print(f"❌ Error seeding sample data: {e}")


# Entry point
if __name__ == "__main__":
    init_db()
    session = SessionLocal()
    try:
        seed_sample_data(session)
    except Exception as e:
        print(f"❌ Error during seeding: {e}")
        raise
    finally:
        session.close()



