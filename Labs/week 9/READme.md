# AI-216 – Programming for Artificial Intelligence
## Lab 09: Model Tuning & Cross-Validation

### Objective
The objective of this lab is to improve machine learning models using model evaluation and optimization techniques. The lab focuses on cross-validation, hyperparameter tuning, model comparison, and final model selection.

---

## Dataset Used

The Wine dataset from scikit-learn was used in this lab.

Dataset loading code:

```python
from sklearn.datasets import load_wine

wine = load_wine()
X = wine.data
y = wine.target
```

---

## Tasks Performed

### Part A – Dataset Preparation

- Loaded Wine dataset
- Converted dataset into Pandas DataFrame
- Assigned feature names
- Added target column
- Displayed dataset information
- Split data into training and testing sets

### Part B – Baseline Model

- Trained Logistic Regression model
- Calculated baseline accuracy

### Part C – Cross Validation

- Applied 5-fold cross-validation
- Obtained cross-validation scores
- Calculated mean accuracy
- Compared results with train-test split

### Part D – Hyperparameter Tuning

Manual tuning was performed using KNN with:

- k = 3
- k = 5
- k = 7
- k = 9

The best value of k was selected based on accuracy.

GridSearchCV was then used to automatically identify the best hyperparameters using 5-fold cross-validation.

---

## Model Comparison

The following models were trained and compared:

1. Logistic Regression
2. K-Nearest Neighbors (KNN)
3. Decision Tree

Cross-validation was used to compare model performance fairly.

---

## Final Model Selection Reasoning

The model with the highest average cross-validation score was selected as the final model.

Reasons:

- Higher prediction accuracy
- Better generalization capability
- More reliable performance across multiple folds

---

## Hyperparameter Tuning Process

Hyperparameter tuning improves model performance by finding optimal values for model parameters.

In this lab:

- Manual tuning tested different K values
- GridSearchCV automated the process
- Best parameters produced improved accuracy

---

## Analysis

### Which model performed best?

The model with the highest cross-validation score performed best.

### Did tuning improve performance?

Yes. Hyperparameter tuning improved performance by selecting optimal parameter values.

### Was cross-validation more reliable than a single split?

Yes. Cross-validation is more reliable because it evaluates the model on multiple subsets of data and reduces overfitting risk.



## Conclusion

This lab demonstrated the importance of:

- Cross-validation
- Hyperparameter tuning
- Model comparison
- Selecting the best machine learning model

These techniques help create more accurate and reliable machine learning systems.