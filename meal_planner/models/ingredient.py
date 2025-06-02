from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from meal_planner.models.base import Base
from meal_planner.models.recipe_ingredient import recipe_ingredient

class Ingredient(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    quantity = Column(String)

    recipes = relationship(
        'Recipe',
        secondary=recipe_ingredient,
        back_populates='ingredients'
    )

    def __repr__(self):
        return f"<Ingredient(id={self.id}, name='{self.name}', quantity='{self.quantity}')>"