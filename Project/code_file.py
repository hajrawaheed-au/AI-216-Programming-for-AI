import pandas as pd
import numpy as np

# OOP Class
class Person:
    def __init__(self, name, age, weight, height_cm, gender):
        self.name   = name
        self.age    = age
        self.weight = weight
        self.height = height_cm
        self.gender = gender

    def bmi(self):
        return round(self.weight / ((self.height / 100) ** 2), 1)

    def bmi_status(self):
        b = self.bmi()
        if b < 18.5: return "Underweight"
        elif b < 25: return "Normal"
        elif b < 30: return "Overweight"
        else:        return "Obese"

    def goal(self):
        b = self.bmi()
        if b < 18.5: return "Gain Weight"
        elif b < 25: return "Maintain Weight"
        else:        return "Lose Weight"

    def daily_calories(self):
        if self.gender == '1':
            bmr = 10 * self.weight + 6.25 * self.height - 5 * self.age + 5
        else:
            bmr = 10 * self.weight + 6.25 * self.height - 5 * self.age - 161
        tdee = bmr * 1.55
        if self.bmi() < 18.5: return int(tdee + 500)
        elif self.bmi() < 25:  return int(tdee)
        else:                  return int(tdee - 500)

# Load & Clean Data
df = pd.read_csv('nutrition.csv')
df = df[['name', 'calories', 'protein', 'carbohydrate', 'fat']].dropna()
for col in ['calories', 'protein', 'carbohydrate', 'fat']:
    df[col] = df[col].astype(str).str.extract(r'([-+]?\d*\.?\d+)')[0].astype(float)

keywords = ['chicken', 'egg', 'rice', 'bread', 'milk', 'banana', 'apple',
            'beef', 'tuna', 'salmon', 'potato', 'oat', 'yogurt', 'cheese',
            'spinach', 'broccoli', 'carrot', 'tomato', 'orange', 'pasta',
            'lentil', 'onion', 'cucumber', 'almond', 'peanut', 'corn', 'fish']
df = df[df['name'].str.lower().str.contains('|'.join(keywords))]
df = df[df['calories'] > 5].drop_duplicates(subset='calories').reset_index(drop=True)

# Meal Plan
def get_foods(keys, n=6):
    return df[df['name'].str.lower().str.contains('|'.join(keys))].head(n).reset_index(drop=True)

def show_meal_plan(cal):
    proteins = get_foods(['chicken', 'tuna', 'salmon', 'egg', 'beef'])
    carbs    = get_foods(['rice', 'bread', 'oat', 'pasta', 'potato'])
    veggies  = get_foods(['spinach', 'broccoli', 'carrot', 'tomato', 'cucumber'])
    fruits   = get_foods(['apple', 'banana', 'orange'])

    meals = [
        ("🌅 Breakfast", int(cal * 0.25), [proteins.iloc[0], carbs.iloc[0],   fruits.iloc[0]]),
        ("☀️  Lunch",    int(cal * 0.35), [proteins.iloc[1], carbs.iloc[1],   veggies.iloc[0]]),
        ("🌙 Dinner",    int(cal * 0.30), [proteins.iloc[2], veggies.iloc[1], veggies.iloc[2]]),
        ("🍎 Snack",     int(cal * 0.10), [fruits.iloc[1],   veggies.iloc[3]]),
    ]

    print(f"\n{'═'*58}\n  🍽️  YOUR PERSONALIZED MEAL PLAN\n{'═'*58}")
    for meal, kcal, foods in meals:
        print(f"\n  {meal}  (~{kcal} kcal)")
        print(f"  {'─'*54}")
        print(f"  {'Food':<40} {'Cal':>5}  {'Pro':>5}  {'Fat':>5}")
        print(f"  {'─'*54}")
        for f in foods:
            print(f"  {f['name'][:39]:<40} {f['calories']:>5.0f}  {f['protein']:>4.1f}g  {f['fat']:>4.1f}g")

# Main
print("\n  ╔══════════════════════════════════════════╗")
print("  ║      🥗  PERSONAL DIET PLANNER  🥗       ║")
print("  ╚══════════════════════════════════════════╝")
print("\n  Enter your details:\n")

name   = input("  Name             : ")
age    = int(input("  Age              : "))
weight = float(input("  Weight (kg)      : "))

print("  Height")
feet   = int(input("    Feet           : "))
inches = int(input("    Inches         : "))
height_cm = round((feet * 30.48) + (inches * 2.54), 1)
print(f"    Converted      : {height_cm} cm")

print("  Gender      1. Male   2. Female")
gender = input("  Choice           : ")

p   = Person(name, age, weight, height_cm, gender)
cal = p.daily_calories()

print(f"\n{'═'*58}")
print(f"  👤 {p.name}  |  Age: {p.age}")
print(f"{'═'*58}")
print(f"  BMI                : {p.bmi()}  →  {p.bmi_status()}")
print(f"  Recommended Goal   : {p.goal()}")
print(f"  Daily Calories     : {cal} kcal")
print(f"  Protein Target     : {int(cal * 0.3 / 4)}g")
print(f"  Carbs Target       : {int(cal * 0.4 / 4)}g")
print(f"  Fat Target         : {int(cal * 0.3 / 9)}g")

print(f"\n{'─'*58}")
print(f"  📊 DATASET STATS (NumPy)")
print(f"{'─'*58}")
print(f"  Avg Calories : {np.mean(df['calories'].values):.1f} kcal")
print(f"  Avg Protein  : {np.mean(df['protein'].values):.1f}g")
print(f"  Avg Carbs    : {np.mean(df['carbohydrate'].values):.1f}g")
print(f"  Avg Fat      : {np.mean(df['fat'].values):.1f}g")

show_meal_plan(cal)

print(f"\n{'═'*58}")
print(f"  Stay consistent and eat healthy! 💪🥗")
print(f"{'═'*58}\n")