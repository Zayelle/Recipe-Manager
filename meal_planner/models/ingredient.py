from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from meal_planner.models.base import Base
from meal_planner.models.recipe_ingredient import RecipeIngredient

class Ingredient(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    recipe_ingredients = relationship(
        "RecipeIngredient",
        back_populates="ingredient",
        cascade="all, delete-orphan"
    )

    @property
    def recipes(self):
        return [ri.recipe for ri in self.recipe_ingredients]

    def __repr__(self):
        return f"<Ingredient(id={self.id}, name='{self.name}')>"

