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
            for ingredient in plan.recipe.ingredients:
                print(f"      - {ingredient.name} ({ingredient.quantity})")
    except Exception as e:
        print(f"❌ Error fetching meal plans: {e}")
    finally:
        session.close()
