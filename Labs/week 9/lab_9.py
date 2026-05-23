import numpy as np
import pandas as pd

from sklearn.datasets import load_wine
from sklearn.model_selection import (
    train_test_split,
    cross_val_score,
    GridSearchCV
)

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

# Part A 

print("\n PART A \n")
wine = load_wine()

X = wine.data
y = wine.target

# Task 1:

df = pd.DataFrame(X, columns=wine.feature_names)

df["target"] = y

print("First 5 rows:")
print(df.head())

print("\nShape of dataset:")
print(df.shape)


# Task 2: 

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42
)

print("\nTraining data shape:", X_train.shape)
print("Testing data shape:", X_test.shape)

# Part B 

print("\n PART B \n")

# Task 3: 

baseline_model = LogisticRegression(max_iter=5000)

baseline_model.fit(X_train, y_train)

y_pred = baseline_model.predict(X_test)

baseline_accuracy = accuracy_score(
    y_test,
    y_pred
)

print("Baseline Accuracy:")
print(round(baseline_accuracy,4))

# Part C 

print("\n PART C\n")

# Task 4:

cv_scores = cross_val_score(
    baseline_model,
    X,
    y,
    cv=5
)

print("Cross Validation Scores:")
print(cv_scores)

mean_cv = cv_scores.mean()

print("\nMean CV Accuracy:")
print(round(mean_cv,4))


# Task 5: 

print("\nComparison:")
print("Baseline Accuracy =", round(baseline_accuracy,4))
print("Cross Validation Mean =", round(mean_cv,4))

if mean_cv > baseline_accuracy:
    print("CV performance slightly better.")
else:
    print("Single split slightly better.")

# Part D 

print("\n PART D \n")

# Task 6: 

k_values = [3,5,7,9]

best_k = 0
best_accuracy = 0

print("Manual KNN Tuning")

for k in k_values:

    knn = KNeighborsClassifier(
        n_neighbors=k
    )

    knn.fit(X_train,y_train)

    pred = knn.predict(X_test)

    acc = accuracy_score(
        y_test,
        pred
    )

    print("k =",k,
          "Accuracy =",round(acc,4))

    if acc > best_accuracy:
        best_accuracy = acc
        best_k = k

print("\nBest K:")
print(best_k)


# Task 7:

print("\nGridSearchCV Results")

parameter_grid = {
    'n_neighbors':[3,5,7,9]
}

grid = GridSearchCV(
    KNeighborsClassifier(),
    parameter_grid,
    cv=5
)

grid.fit(X_train,y_train)

print("Best Parameters:")
print(grid.best_params_)

print("Best Score:")
print(round(grid.best_score_,4))


# Part E

print("\n PART E \n")

models = {

    "Logistic Regression":
        LogisticRegression(max_iter=5000),

    "KNN":
        KNeighborsClassifier(
            n_neighbors=grid.best_params_[
                'n_neighbors'
            ]
        ),

    "Decision Tree":
        DecisionTreeClassifier(
            random_state=42
        )
}


results = {}

for name,model in models.items():

    scores = cross_val_score(
        model,
        X,
        y,
        cv=5
    )

    results[name] = scores.mean()


print("Model Performance")

for name,score in results.items():

    print(
        name,
        "=",
        round(score,4)
    )

# Part F 

print("\n========== PART F ==========\n")

# Task 9

best_model_name = max(
    results,
    key=results.get
)

print("Best Model:")
print(best_model_name)

best_model = models[
    best_model_name
]

best_model.fit(
    X_train,
    y_train
)

final_predictions = best_model.predict(
    X_test
)

final_accuracy = accuracy_score(
    y_test,
    final_predictions
)

print("\nFinal Test Accuracy:")
print(round(final_accuracy,4))

# Task 10 

print("\n ANALYSIS \n")

print("1. Best Model:")
print(best_model_name)

print("\n2. Did tuning improve performance?")
print(
"Tuning improves model performance because \
optimal parameters are selected."
)

print("\n3. Was cross-validation more reliable?")
print(
"Yes, because cross-validation evaluates \
multiple data splits and reduces bias."
)
