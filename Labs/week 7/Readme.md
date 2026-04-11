# Week 07 — Data Preprocessing Pipeline (Applicants Dataset)

##  Brief Description of Tasks

This project builds a full data preprocessing pipeline using Pandas to prepare raw applicant data for machine learning.

### Task 1 — Load and Inspect Data
In this task, we loaded CSV and JSON files into Pandas DataFrames and explored the data using:
- `.head()` to view sample rows
- `.dtypes` to check data types
- `.isnull().sum()` to find missing values
- `.shape` to understand dataset size

This step helps identify issues before any cleaning begins.

---

### Task 2 — Merge Datasets
We merged two datasets (`applicants.csv` and `applicants_extra.json`) using the `id` column.  
A **left join** was used to ensure no applicant is lost from the main dataset even if extra information is missing.

---

### Task 3 — Handle Missing Values
We handled missing data using different strategies:
- Age → filled with median
- Experience → filled with 0
- Expected salary → replaced "?" with NaN, then filled with median
- Education → filled with "Unknown"
- Name → filled with "Unknown"

---

### Task 4 — Clean Inconsistent Data
We standardized the `city` column by:
- Replacing `"isl"` with `"Islamabad"`
- Converting all values to lowercase

This ensures consistency in categorical values.

---

### Task 5 — Feature Engineering
We created a new feature called `experience_level`:
- 0–1 years → junior
- 2–5 years → mid
- 6+ years → senior

This helps convert numeric data into meaningful categories.

---

### Task 6 — Normalize Numeric Features
We applied Min-Max normalization to:
- age
- experience
- expected_salary

This scales values between **0 and 1**, preventing large-value features from dominating others.

---

### Task 7 — Preprocessing Function
We combined all steps into a reusable function so the same preprocessing can be applied to any new dataset consistently.

---

### Task 8 — Skills Feature Engineering (Optional)
We processed the `skills` column by:
- Counting number of skills (`skill_count`)
- Extracting all unique skills
- Creating binary columns like `has_python`, `has_sql`

---

##  Preprocessing Decisions

### Decision 1 — Using Median Instead of Mean
We used median for age and salary because it is more robust to outliers. Mean can be heavily affected by extreme values, which can distort the dataset.

---

### Decision 2 — Filling Missing Experience with 0
We assumed missing experience means the applicant has no recorded work experience. This is a reasonable assumption in hiring datasets, although it may not always be correct in all real-world cases.

---

##  Challenge / Surprise

The most difficult part was handling the value `"?"` in the `expected_salary` column.  
Pandas did not automatically detect it as missing, so it had to be manually replaced with `NaN` before applying imputation.

This shows that real-world data often contains non-standard missing values.

---

##  Pipeline Scaling Question

### If 100 new applicants were submitted tomorrow, what would you need to change in your pipeline?

If new applicants arrive, the pipeline must be improved in the following ways:

- The preprocessing function must be automatically applied to all new incoming data
- All transformation rules (median, normalization, etc.) should be learned from training data and reused, not recalculated every time
- Encoding of features (like skills and experience_level) must remain consistent with training structure
- The pipeline should be saved and reused (e.g., using a serialized preprocessing pipeline or sklearn Pipeline)

This ensures that new data is processed in exactly the same way as training data, which is critical for reliable machine learning predictions.