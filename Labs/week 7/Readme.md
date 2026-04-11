# Week 07 — Data Preprocessing Pipeline (Applicants Dataset)

##  Overview
This project focuses on building a complete data preprocessing pipeline using Pandas. It includes data loading, inspection, cleaning, merging, feature engineering, normalization, and preparing the dataset for machine learning workflows.

---

##  Task Descriptions

### Task 1 — Load and Inspect Data
We created CSV and JSON files and loaded them into Pandas DataFrames.  
We inspected:
- First 5 rows
- Data types
- Missing values per column
- Dataset shape

This helped identify data quality issues before cleaning.

---

### Task 2 — Merge Datasets
We merged:
- `applicants.csv`
- `applicants_extra.json`

on the `id` column using a **left join**, ensuring all applicants remain in the dataset even if extra information is missing.

---

### Task 3 — Handle Missing Values
We handled missing data using appropriate strategies:
- age → filled with median
- experience → filled with 0
- expected_salary → replaced "?" with NaN, then filled with median
- education → filled with "Unknown"
- name → filled with "Unknown"

---

### Task 4 — Clean Inconsistent Data
We standardized the `city` column by:
- Replacing `"isl"` with `"Islamabad"`
- Converting all values to lowercase

This ensured consistent categorical values.

---

### Task 5 — Feature Engineering
We created a new feature:
- `experience_level`

Based on rules:
- 0–1 years → junior
- 2–5 years → mid
- 6+ years → senior

---

### Task 6 — Normalize Numeric Features
We applied Min-Max normalization to:
- age
- experience
- expected_salary

All values were scaled to the range `[0, 1]`.

---

### Task 7 — Preprocessing Function
We combined all preprocessing steps into a reusable function:

```python
def preprocess_applicants(df):
    return df_clean