from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from meal_planner.models.base import Base

class MealPlan(Base):
    __tablename__ = 'meal_plans'

    id = Column(Integer, primary_key=True)
    day = Column(String, nullable=False)
    recipe_id = Column(Integer, ForeignKey('recipes.id'), nullable=False)

    recipe = relationship('Recipe',backref='meal_plans')
    def __repr__(self):
        return f"<MealPlan(id=(day='{self.day}', recipe={self.recipe_name})>"
