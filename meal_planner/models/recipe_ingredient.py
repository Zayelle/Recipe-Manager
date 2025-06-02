from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from meal_planner.database.setup import Base

class RecipeIngredient(Base):
    __tablename__ = "recipe_ingredient"

    recipe_id = Column(Integer, ForeignKey("recipes.id"), primary_key=True)
    ingredient_id = Column(Integer, ForeignKey("ingredients.id"), primary_key=True)
    quantity = Column(Float)

    recipe = relationship("Recipe", back_populates="recipe_ingredients")
    ingredient = relationship("Ingredient", back_populates="recipe_ingredients")

    def __repr__(self):
        return f"<RecipeIngredient(recipe_id={self.recipe_id}, ingredient_id={self.ingredient_id}, quantity={self.quantity})>"

