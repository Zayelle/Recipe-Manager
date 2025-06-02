from meal_planner.database import SessionLocal, init_db
from meal_planner.models.recipe import Recipe
from meal_planner.models.ingredient import Ingredient


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
        return recipe
    recipe = Recipe(name=name)
    recipe.ingredients = ingredients
    session.add(recipe)
    return recipe

def seed_sample_data(session):
    print("Seeding sample recipes and ingredients...")

    rice = get_or_create_ingredient(session, "Rice", 200)
    chicken = get_or_create_ingredient(session, "Chicken Breast", 300)
    broccoli = get_or_create_ingredient(session, "Broccoli", 150)
    eggs = get_or_create_ingredient(session, "Eggs", 2)
    tomato = get_or_create_ingredient(session, "Tomato", 100)
    pasta = get_or_create_ingredient(session, "Pasta", 250)
    cheese = get_or_create_ingredient(session, "Cheese", 100)

    get_or_create_recipe(session, "Chicken Rice Bowl", [rice, chicken, broccoli])
    get_or_create_recipe(session, "Tomato Pasta", [pasta, tomato, cheese])
    get_or_create_recipe(session, "Veggie Omelette", [eggs, tomato, broccoli])

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

