# 🥗 Personal Diet Planner

A Python-based diet planning tool that takes your personal details and automatically recommends a personalized daily meal plan based on your BMI and calorie needs — no manual goal selection required.

---

## 🚀 What It Does

- Calculates your **BMI** and health status automatically
- Detects your **diet goal** (Lose / Gain / Maintain) based on BMI
- Calculates **daily calorie needs** using the BMR formula
- Recommends a **full day meal plan** — Breakfast, Lunch, Dinner & Snack
- Shows **nutrition stats** from the dataset using NumPy

---

## 🛠️ Built With

- **Python**
- **Pandas** — data loading & filtering
- **NumPy** — nutrition statistics
- **nutrition.csv** — dataset of 8,789 real food items

---

## 📂 Project Structure

```
📦 diet-planner/
├── diet_planner.py    ← main program
├── nutrition.csv      ← nutrition dataset
└── README.md
```

---

## ▶️ How to Run

1. Make sure `diet_planner.py` and `nutrition.csv` are in the same folder
2. Run in terminal:

```bash
python diet_planner.py
```

3. Enter your details:

```
Name             : Hajra
Age              : 21
Weight (kg)      : 55
Height
  Feet           : 5
  Inches         : 4
Gender      1. Male   2. Female
Choice           : 2
```

---

## 📊 Sample Output

```
╔══════════════════════════════════════════╗
║      🥗  PERSONAL DIET PLANNER  🥗       ║
╚══════════════════════════════════════════╝

  👤 Hajra  |  Age: 21
══════════════════════════════════════════════
  BMI                : 21.3  →  Normal
  Recommended Goal   : Maintain Weight
  Daily Calories     : 1920 kcal
  Protein Target     : 144g
  Carbs Target       : 192g
  Fat Target         : 64g

  📊 DATASET STATS (NumPy)
  Avg Calories : 198.4 kcal
  Avg Protein  : 11.3g
  Avg Carbs    : 22.1g
  Avg Fat      : 10.6g

  🍽️  YOUR PERSONALIZED MEAL PLAN

  🌅 Breakfast (~480 kcal)
  Chicken breast, roasted          165   31.0g   3.6g
  Rice, white, cooked              130    2.7g   0.3g
  Apple, raw                        52    0.3g   0.2g

  ☀️  Lunch (~672 kcal)
  Tuna, canned in water             86   19.4g   0.9g
  Bread, whole wheat               247   13.0g   3.4g
  Spinach, raw                      23    2.9g   0.4g

  🌙 Dinner (~576 kcal)
  Salmon, Atlantic, cooked         206   20.4g  12.3g
  Broccoli, cooked                  35    2.4g   0.4g
  Carrot, raw                       41    0.9g   0.2g

  🍎 Snack (~192 kcal)
  Banana, raw                       89    1.1g   0.3g
  Tomato, red, raw                  18    0.9g   0.2g
```

---

## ⚙️ How It Works

**BMI Formula**
```
BMI = weight(kg) / height(m)²
```

**BMR Formula (Mifflin-St Jeor)**
```
Male   → (10 × weight) + (6.25 × height) − (5 × age) + 5
Female → (10 × weight) + (6.25 × height) − (5 × age) − 161

Daily Calories = BMR × 1.55
```

**Goal Detection**
| BMI | Status | Goal |
|---|---|---|
| < 18.5 | Underweight | Gain Weight |
| 18.5 – 24.9 | Normal | Maintain Weight |
| 25+ | Overweight / Obese | Lose Weight |

---

## 📦 Requirements

```bash
pip install pandas numpy
```
