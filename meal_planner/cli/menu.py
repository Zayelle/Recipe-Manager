def main_menu():
    print("\nPlease choose an option:")
    print("1. View all recipes")
    print("2. Add a new recipe")
    print("3. Plan meals for the week")
    print("4. View weekly meal plan")
    print("5. Generate grocery list")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ").strip()

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
        print("Exiting... Goodbye!")
        exit()
    else:
        print("Invalid choice. Please try again.")


def view_all_recipes():
    print("\n[Placeholder] Showing all recipes...")
    # TODO: Connect to DB and list recipes


def add_new_recipe():
    print("\n[Placeholder] Add a new recipe...")
    # TODO: Prompt for recipe details and save to DB


def plan_meals():
    print("\n[Placeholder] Plan meals for the week...")
    # TODO: Add logic for meal planning


def view_weekly_plan():
    print("\n[Placeholder] View your weekly meal plan...")
    # TODO: Retrieve and display the meal plan


def generate_grocery_list():
    print("\n[Placeholder] Generate grocery list from plan...")
    # TODO: Generate shopping list based on meals
