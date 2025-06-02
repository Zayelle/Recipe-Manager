from meal_planner.cli.menu import main_menu
from meal_planner.database.setup import init_db, SessionLocal
from meal_planner.seed.seed_data import seed_sample_data
from meal_planner.models.ingredient import Ingredient


def setup_database():
    init_db()  # Create tables

    # Check if data exists, then seed if empty
    session = SessionLocal()
    try:
        if not session.query(Ingredient).first():
            seed_sample_data(session)
    except Exception as e:
        print(f"❌ Failed to seed data: {e}")
    finally:
        session.close()

def main():
    print("Welcome to the Recipe Manager & Meal Planner CLI!")
    setup_database()  # Initialize the database and seed data
    while True:
        try:
            main_menu()
        except KeyboardInterrupt:
            print("\nExiting the application. Goodbye!")
            break

if __name__ == "__main__":
    main()
