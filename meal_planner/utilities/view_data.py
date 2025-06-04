import csv
from meal_planner.database import SessionLocal
from meal_planner.models.meal_plan import MealPlan

def view_meal_plans():
    session = SessionLocal()
    try:
        meal_plans = session.query(MealPlan).all()
        if not meal_plans:
            print("📭 No meal plans found.")
            return

        print("\n📅 Weekly Meal Plan:")
        for plan in meal_plans:
            print(f"\n🗓️  {plan.day}")
            print(f"   🍽️  Recipe: {plan.recipe.name}")
            print("   🧂 Ingredients:")
            for ingredient, quantity in plan.recipe.ingredients:
                print(f"      - {ingredient.name} ({quantity})")
    except Exception as e:
        print(f"❌ Error fetching meal plans: {e}")
    finally:
        session.close()

def export_meal_plan_to_csv(meal_plans, filename="meal_plan.csv"):
    try:
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Day", "Recipe"])
            for plan in meal_plans:
                writer.writerow([plan.day, plan.recipe.name])
        print(f"\n✅ Meal plan exported to {filename}")
    except Exception as e:
        print(f"\n❌ Failed to export meal plan: {e}")

def export_recipes_to_csv(recipes, filename="recipes.csv"):
    try:
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Instructions", "Ingredients"])

            for recipe in recipes:
                ingredients = ", ".join([
                    f"{ri.ingredient.name} ({ri.quantity})"
                    for ri in recipe.recipe_ingredients
                ]) or "N/A"

                writer.writerow([recipe.name, recipe.instructions or "N/A", ingredients])

        print(f"\n✅ Recipes exported to {filename}")
    except Exception as e:
        print(f"\n❌ Failed to export recipes: {e}")


def export_ingredients_to_csv(ingredients, filename="ingredients.csv"):
    try:
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Used In Recipes (Quantity)"])

            for ingredient in ingredients:
                recipes = ", ".join([
                    f"{ri.recipe.name} ({ri.quantity})"
                    for ri in ingredient.recipe_ingredients
                ]) or "N/A"

                writer.writerow([ingredient.name, recipes])

        print(f"\n✅ Ingredients exported to {filename}")
    except Exception as e:
        print(f"\n❌ Failed to export ingredients: {e}")




