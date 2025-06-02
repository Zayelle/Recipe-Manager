from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from meal_planner.models.base import Base
from meal_planner.models.recipe_ingredient import RecipeIngredient  # the class, not the table

class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    meal_type = Column(String)
    instructions = Column(Text)

    recipe_ingredients = relationship(
        "RecipeIngredient",
        back_populates="recipe",
        cascade="all, delete-orphan"
    )

    @property
    def ingredients(self):
        # Return list of (Ingredient object, quantity)
        return [(ri.ingredient, ri.quantity) for ri in self.recipe_ingredients]

    def __repr__(self):
        return f"<Recipe(id={self.id}, name='{self.name}', meal_type='{self.meal_type}', instructions='{(self.instructions or '')[:30]}...')>"

