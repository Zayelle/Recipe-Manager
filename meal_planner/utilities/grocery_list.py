def generate_grocery_list_from_plan(meal_plan):
    """
    Given a meal plan (list of Recipe objects), generate a grocery list
    by aggregating all required ingredients.

    :param meal_plan: List of Recipe objects
    :return: Dict with ingredient names as keys and quantities as values
    """
    grocery_list = {}

    for recipe in meal_plan:
        for ingredient in recipe.ingredients:
            name = ingredient.name
            qty = ingredient.quantity
            if name in grocery_list:
                grocery_list[name].append(qty)
            else:
                grocery_list[name] = [qty]

    return grocery_list
