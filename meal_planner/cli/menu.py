from meal_planner.database import SessionLocal
from meal_planner.models.recipe import Recipe
from meal_planner.models.meal_plan import MealPlan
from meal_planner.models.ingredient import Ingredient
from meal_planner.utilities.grocery_list import generate_grocery_list_from_plan, export_grocery_list_to_csv
from meal_planner.seed.seed_data import seed_sample_data
from meal_planner.utilities.view_data import export_meal_plan_to_csv
from meal_planner.utilities.view_data import export_recipes_to_csv
from meal_planner.utilities.view_data import export_ingredients_to_csv

def main_menu():
    print("\nPlease choose an option:")
    print("1. View all recipes")
    print("2. Add a new recipe")
    print("3. Plan meals for the week")
    print("4. View weekly meal plan")
    print("5. Generate grocery list")
    print("6. Seed sample data") 
    print("7. Exit")

    choice = input("Enter your choice (1-7): ").strip()

    if choice == "1":
        view_all_recipes()
    elif choice == "2":
        add_new_recipe()
    elif choice == "3":
        plan_meals()
    elif choice == "4":
        view_weekly_plan()
    elif choice == "5":
        generate_grocery_list()
    elif choice == "6":
        seed_data_command()
    elif choice == "7":
        view_all_ingredients()
    elif choice == "8":
        print("Exiting... Goodbye!")
        exit()
    else:
        print("Invalid choice. Please try again.")

# ✅ View All Recipes
def view_all_recipes():
    session = SessionLocal()
    print("\n📖 All Recipes:")
    try:
        recipes = session.query(Recipe).all()
        if not recipes:
            print("No recipes found.")
        else:
            for recipe in recipes:
                print(f"\n📝 {recipe.name}\nInstructions: {recipe.instructions or 'N/A'}")

            export = input("\n📤 Export recipes to CSV? (y/n): ").strip().lower()
            if export == "y":
                export_recipes_to_csv(recipes)

    except Exception as e:
        print(f"❌ Error fetching recipes: {e}")
    finally:
        session.close()


# ✅ Add a New Recipe
def add_new_recipe():
    print("\n➕ Add a New Recipe")
    name = input("Enter recipe name: ").strip()
    instructions = input("Enter cooking instructions: ").strip()

    if not name:
        print("❌ Recipe name cannot be empty.")
        return

    session = SessionLocal()
    new_recipe = Recipe(name=name, instructions=instructions)

    try:
        session.add(new_recipe)
        session.commit()
        print(f"✅ Recipe '{new_recipe.name}' added successfully.")
    except Exception as e:
        session.rollback()
        print(f"❌ Failed to add recipe: {e}")
    finally:
        session.close()

def plan_meals():
    session = SessionLocal()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    try:
        recipes = session.query(Recipe).all()
        if not recipes:
            print("❌ No recipes available. Add some recipes first.")
            return

        print("\n📅 Plan Your Week:")
        for day in days:
            print(f"\n--- {day} ---")
            for idx, recipe in enumerate(recipes, start=1):
                print(f"{idx}. {recipe.name}")
            choice = input(f"Select a recipe number for {day} (or leave blank to skip): ").strip()

            if choice.isdigit():
                index = int(choice) - 1
                if 0 <= index < len(recipes):
                    selected_recipe = recipes[index]
                    plan = MealPlan(day=day, recipe=selected_recipe)
                    session.add(plan)

        session.commit()
        print("\n✅ Weekly meal plan saved.")
    except Exception as e:
        session.rollback()
        print(f"❌ Error planning meals: {e}")
    finally:
        session.close()

def view_weekly_plan():
    session = SessionLocal()
    try:
        plans = session.query(MealPlan).order_by(MealPlan.day).all()
        if not plans:
            print("\n📭 No meal plan found.")
        else:
            print("\n📆 Weekly Meal Plan:")
            for plan in plans:
                print(f"{plan.day}: {plan.recipe.name}")

            # Offer export
            export = input("\n📤 Export meal plan to CSV? (y/n): ").strip().lower()
            if export == "y":
                export_meal_plan_to_csv(plans)

    except Exception as e:
        print(f"❌ Error viewing plan: {e}")
    finally:
        session.close()

def generate_grocery_list():
    session = SessionLocal()
    try:
        meal_plans = session.query(MealPlan).all()

        if not meal_plans:
            print("\n⚠️ No meal plans found. Please plan your meals first.")
            return

        recipes = list({plan.recipe for plan in meal_plans})
        grocery_list = generate_grocery_list_from_plan(recipes)

        print("\n🛒 Grocery List:")
        for ingredient, quantity in grocery_list.items():
            print(f"- {ingredient}: {quantity}")

        # Ask if user wants to export to CSV
        export = input("\n📤 Export grocery list to CSV? (y/n): ").strip().lower()
        if export == "y":
            export_grocery_list_to_csv(grocery_list)

    except Exception as e:
        print(f"\n❌ Error generating grocery list: {e}")
    finally:
        session.close()


def seed_data_command():
    session = SessionLocal()
    try:
        seed_sample_data(session)
        print("✅ Sample data seeded successfully.")
    except Exception as e:
        print(f"❌ Error seeding sample data: {e}")
    finally:
        session.close()
    
def view_all_ingredients():
    session = SessionLocal()
    try:
        ingredients = session.query(Ingredient).all()
        if not ingredients:
            print("\n📭 No ingredients found.")
        else:
            print("\n🧂 All Ingredients:")
            for ing in ingredients:
                print(f"- {ing.name}: {ing.quantity or 'unspecified'}")

            export = input("\n📤 Export ingredients to CSV? (y/n): ").strip().lower()
            if export == "y":
                export_ingredients_to_csv(ingredients)
    except Exception as e:
        print(f"❌ Error fetching ingredients: {e}")
    finally:
        session.close()     

    
