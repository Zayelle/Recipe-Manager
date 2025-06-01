# meal_planner/models/recipe.py
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from meal_planner.models.base import Base
from meal_planner.models.recipe_ingredient import recipe_ingredient

class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    meal_type = Column(String)
    instructions = Column(Text)

    ingredients = relationship(
        'Ingredient',
        secondary=recipe_ingredient,
        back_populates='recipes'
    )
