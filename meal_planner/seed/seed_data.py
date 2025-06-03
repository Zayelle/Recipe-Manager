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

    # RecipeIngredients
    ri_1 = [
        RecipeIngredient(ingredient=rice, quantity=200.0),
        RecipeIngredient(ingredient=chicken, quantity=300.0),
        RecipeIngredient(ingredient=broccoli, quantity=150.0),
    ]
    rice_bowl.recipe_ingredients = ri_1
    session.add_all(ri_1)

    ri_2 = [
        RecipeIngredient(ingredient=pasta, quantity=250.0),
        RecipeIngredient(ingredient=tomato, quantity=100.0),
        RecipeIngredient(ingredient=cheese, quantity=100.0),
    ]
    tomato_pasta.recipe_ingredients = ri_2
    session.add_all(ri_2)

    ri_3 = [
        RecipeIngredient(ingredient=eggs, quantity=2.0),
        RecipeIngredient(ingredient=tomato, quantity=100.0),
        RecipeIngredient(ingredient=broccoli, quantity=150.0),
    ]
    omelette.recipe_ingredients = ri_3
    session.add_all(ri_3)

    # Add recipes (if not already managed)
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
        if not session.query(MealPlan).filter_by(day=day).first():
            session.add(MealPlan(day=day, recipe=recipe))

    session.commit()
    print(f"✅ Seeded {session.query(Recipe).count()} recipes, {session.query(Ingredient).count()} ingredients.")

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



