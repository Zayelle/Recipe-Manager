from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from meal_planner.models.base import Base
# Define the database URL (you can change 'meal_planner.db' to something else if needed)
DATABASE_URL = "sqlite:///meal_planner.db"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=False)

# Create a configured session class
SessionLocal = sessionmaker(bind=engine)

# Base class for models to inherit
Base = declarative_base()

def init_db():
    """
    Import all models and create tables.
    """
    from meal_planner.models import recipe, ingredient, recipe_ingredient, meal_plan  # type: ignore
    Base.metadata.create_all(bind=engine)
