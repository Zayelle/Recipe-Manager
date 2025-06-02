from meal_planner.database import SessionLocal, init_db
from meal_planner.models.recipe import Recipe
from meal_planner.models.ingredient import Ingredient
from meal_planner.models.meal_plan import MealPlan


def get_or_create_ingredient(session, name, quantity):
    ingredient = session.query(Ingredient).filter_by(name=name).first()
    if ingredient:
        print(f"✔ Ingredient exists: {name}")
        return ingredient
    ingredient = Ingredient(name=name, quantity=quantity)
    session.add(ingredient)
    print(f"➕ Added new ingredient: {name}")
    return ingredient

def get_or_create_recipe(session, name, ingredients):
    recipe = session.query(Recipe).filter_by(name=name).first()
    if recipe:
        print(f"✔ Recipe exists: {name}")
        return recipe
    recipe = Recipe(name=name)
    recipe.ingredients = ingredients
    session.add(recipe)
    print(f"➕ Added new recipe: {name}")
    return recipe

def seed_sample_data(session):
    print("🌱 Seeding sample recipes and ingredients...")

    # Ingredients
    rice = get_or_create_ingredient(session, "Rice", "200g")
    chicken = get_or_create_ingredient(session, "Chicken Breast", "300g")
    broccoli = get_or_create_ingredient(session, "Broccoli", "150g")
    eggs = get_or_create_ingredient(session, "Eggs", "2")
    tomato = get_or_create_ingredient(session, "Tomato", "100g")
    pasta = get_or_create_ingredient(session, "Pasta", "250g")
    cheese = get_or_create_ingredient(session, "Cheese", "100g")

    # Recipes
    rice_bowl = get_or_create_recipe(session, "Chicken Rice Bowl", [rice, chicken, broccoli])
    tomato_pasta = get_or_create_recipe(session, "Tomato Pasta", [pasta, tomato, cheese])
    omelette = get_or_create_recipe(session, "Veggie Omelette", [eggs, tomato, broccoli])

    # Meal Plans
    meal_plans = [
        MealPlan(day="Monday", recipe=rice_bowl),
        MealPlan(day="Tuesday", recipe=tomato_pasta),
        MealPlan(day="Wednesday", recipe=omelette)
    ]
    session.add_all(meal_plans)

    session.commit()
    print("✅ Seeding completed!")

# Entry point
if __name__ == "__main__":
    init_db()
    session = SessionLocal()
    try:
        seed_sample_data(session)
    except Exception as e:
        print(f"❌ Error during seeding: {e}")
    finally:
        session.close()


