from meal_planner.cli.menu import main_menu

def main():
    print("Welcome to the Recipe Manager & Meal Planner CLI!")
    while True:
        try:
            main_menu()
        except KeyboardInterrupt:
            print("\nExiting the application. Goodbye!")
            break

if __name__ == "__main__":
    main()
