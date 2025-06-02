# Recipe-Manager
# 🥗 Meal Planner CLI

A command-line application that helps users manage recipes, plan meals for the week, and generate grocery lists automatically.

Built with **Python**, **SQLAlchemy ORM**, and managed using **Pipenv**.

---

## 📌 Features

- Add and view recipes with ingredients and instructions
- Plan meals for each day of the week
- Generate grocery lists based on your meal plan
- Persistent data storage using SQLite via SQLAlchemy ORM
- Simple and intuitive CLI interface

---

## 📁 Project Structure

meal_planner/
├── cli/
│ ├── init.py
│ └── menu.py # CLI interactions and user prompts
│
├── database/
│ ├── init.py
│ └── setup.py # SQLAlchemy engine/session setup
│
├── models/
│ ├── init.py
│ ├── recipe.py # Recipe model
│ ├── ingredient.py # Ingredient model
│ ├── recipe_ingredient.py # Association table for many-to-many
│ └── meal_plan.py # MealPlan model
│
├── utils/
│ ├── init.py
│ └── grocery_list.py # Logic to generate shopping lists
│
├── main.py # Entry point for the CLI app
├── Pipfile # Pipenv environment file
├── Pipfile.lock # Pipenv lock file (auto-generated)
└── README.md # Project overview and setup instructions


---

## ⚙️ Setup Instructions

### 1. Clone the Repo
```bash
git clone https://github.com/Zayelle/Recipe-Manager.git
cd meal-planner-cli


