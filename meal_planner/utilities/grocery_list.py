import re
from typing import List, Dict, Union
from collections import defaultdict
from meal_planner.database.setup import SessionLocal
from meal_planner.models.meal_plan import MealPlan
from meal_planner.models.recipe import Recipe

def parse_quantity(qty):
    """
    Parse a quantity like '200g' or '2' into (amount, unit).
    Returns (amount, unit) if possible, else (None, None).
    """
    if isinstance(qty, (int, float)):
        return qty, ""
    match = re.match(r"^\s*(\d+(?:\.\d+)?)([a-zA-Z]*)\s*$", str(qty))
    if match:
        amount, unit = match.groups()
        return float(amount), unit
    return None, None

def generate_grocery_list_from_plan(meal_plan: List['Recipe']) -> Dict[str, Union[str, List[str]]]:
    """
    Given a list of Recipe objects, generate a grocery list by summing quantities.

    :param meal_plan: List of Recipe objects
    :return: Dict of ingredient name -> total quantity (str) or list if mixed
    """
    grocery_list = defaultdict(list)

    for recipe in meal_plan:
        for ingredient in recipe.ingredients:
            name = ingredient.name
            qty = ingredient.quantity or "unspecified"
            grocery_list[name].append(qty)

    combined_grocery = {}
    for name, qty_list in grocery_list.items():
        parsed = [parse_quantity(q) for q in qty_list]
        all_numeric = all(a is not None for a, _ in parsed)

        if all_numeric:
            unit_set = set(u for _, u in parsed)
            if len(unit_set) == 1:
                unit = unit_set.pop()
                total = sum(a for a, _ in parsed)
                combined_grocery[name] = f"{total:.0f}{unit}" if unit else f"{total:.0f}"
            else:
                combined_grocery[name] = ", ".join(qty_list)
        else:
            combined_grocery[name] = ", ".join(qty_list)

    return combined_grocery

def print_grocery_list(grocery_list):
    print("\n🛒 Grocery List:")
    if not grocery_list:
        print("  (No ingredients found)")
    for name, qty in grocery_list.items():
        print(f" - {name}: {qty}")

def generate_grocery_list():
    session = SessionLocal()
    try:
        meal_plans = session.query(MealPlan).all()
        if not meal_plans:
            print("\n⚠️ No meal plans found. Please plan your meals first.")
            return

        recipes = list({plan.recipe for plan in meal_plans})
        grocery_list = generate_grocery_list_from_plan(recipes)
        print_grocery_list(grocery_list)

    except Exception as e:
        print(f"\n❌ Error generating grocery list: {e}")
    finally:
        session.close()
