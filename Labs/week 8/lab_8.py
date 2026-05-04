#Part A
from sklearn.datasets import load_wine
import pandas as pd

wine = load_wine()
X = wine.data
y = wine.target

df = pd.DataFrame(X, columns=wine.feature_names)
df['target'] = y

print("=== First 5 Rows ===")
print(df.head())

print("\n=== Dataset Shape ===")
print("Shape:", df.shape)

print("\n=== Class Distribution ===")
print(df['target'].value_counts())

print("\n=== Feature and Target Separation ===")
X = df.drop('target', axis=1)
y = df['target']
print("X shape:", X.shape)
print("y shape:", y.shape)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)
print("\n=== Train-Test Split ===")
print("Training set shape:", X_train.shape)
print("Testing set shape: ", X_test.shape)

#Part B
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

wine = load_wine()
X, y = wine.data, wine.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

print("=== Logistic Regression ===")
lr_model = LogisticRegression(max_iter=10000, random_state=42)
lr_model.fit(X_train, y_train)
lr_preds = lr_model.predict(X_test)
print("Predictions:", lr_preds)

print("\n=== KNN Classifier (k=5) ===")
knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train, y_train)
knn_preds = knn_model.predict(X_test)
print("Predictions:", knn_preds)

print("\n=== Prediction Comparison ===")
print(f"Matching predictions: {sum(lr_preds == knn_preds)} / {len(lr_preds)}")

#Part C
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

wine = load_wine()
X, y = wine.data, wine.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

lr_model = LogisticRegression(max_iter=10000, random_state=42)
lr_model.fit(X_train, y_train)
lr_preds = lr_model.predict(X_test)

knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train, y_train)
knn_preds = knn_model.predict(X_test)

print("=== Task 5: Accuracy Evaluation ===")
lr_acc  = accuracy_score(y_test, lr_preds)
knn_acc = accuracy_score(y_test, knn_preds)
print(f"Logistic Regression Accuracy: {lr_acc:.4f}")
print(f"KNN Accuracy:                 {knn_acc:.4f}")
if lr_acc > knn_acc:
    print(">> Logistic Regression performs better.")
else:
    print(">> KNN performs better.")

print("\n=== Task 6: Confusion Matrix (Logistic Regression) ===")
cm = confusion_matrix(y_test, lr_preds)
print("Confusion Matrix:\n", cm)

TP = cm[0, 0]
FP = cm[1, 0] + cm[2, 0]
FN = cm[0, 1] + cm[0, 2]
TN = cm[1, 1] + cm[1, 2] + cm[2, 1] + cm[2, 2]
print(f"\nFor Class 0 (one-vs-rest):")
print(f"  TP={TP}, FP={FP}, FN={FN}, TN={TN}")
print("Error analysis: Any FP means the model wrongly predicted class 0.")
print("Any FN means the model missed an actual class 0 sample.")

print("\n=== Task 7: Classification Report (Logistic Regression) ===")
print(classification_report(
    y_test, lr_preds,
    target_names=wine.target_names
))

#Task D
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

wine = load_wine()
X, y = wine.data, wine.target

print("=== Task 8: Feature Experimentation ===")

X_1feat = wine.data[:, [0]]
X_tr1, X_ts1, y_tr1, y_ts1 = train_test_split(
    X_1feat, y, test_size=0.25, random_state=42
)
lr_1 = LogisticRegression(max_iter=10000)
lr_1.fit(X_tr1, y_tr1)
acc_1 = accuracy_score(y_ts1, lr_1.predict(X_ts1))
print(f"1 Feature  (alcohol only):        Accuracy = {acc_1:.4f}")

X_2feat = wine.data[:, [0, 1]]
X_tr2, X_ts2, y_tr2, y_ts2 = train_test_split(
    X_2feat, y, test_size=0.25, random_state=42
)
lr_2 = LogisticRegression(max_iter=10000)
lr_2.fit(X_tr2, y_tr2)
acc_2 = accuracy_score(y_ts2, lr_2.predict(X_ts2))
print(f"2 Features (alcohol + malic acid): Accuracy = {acc_2:.4f}")

X_tr_all, X_ts_all, y_tr_all, y_ts_all = train_test_split(
    X, y, test_size=0.25, random_state=42
)
lr_all = LogisticRegression(max_iter=10000, random_state=42)
lr_all.fit(X_tr_all, y_tr_all)
acc_all = accuracy_score(y_ts_all, lr_all.predict(X_ts_all))
print(f"All Features (13):                 Accuracy = {acc_all:.4f}")
print(">> More informative features = better accuracy.")

print("\n=== Task 9: Changing Train-Test Ratio ===")

for split in [0.25, 0.50]:
    X_tr, X_ts, y_tr, y_ts = train_test_split(
        X, y, test_size=split, random_state=42
    )
    lr = LogisticRegression(max_iter=10000, random_state=42)
    lr.fit(X_tr, y_tr)
    acc = accuracy_score(y_ts, lr.predict(X_ts))
    print(f"test_size={split} | Train={len(X_tr)} | Test={len(X_ts)} | Accuracy={acc:.4f}")

print(">> Smaller training set generally reduces model accuracy.")

#Task E
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

def run_pipeline(model, model_name, X_train, X_test, y_train, y_test):

    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    acc = accuracy_score(y_test, preds)
    cm  = confusion_matrix(y_test, preds)

    print(f"Model           : {model_name}")
    print(f"Accuracy Score  : {acc:.4f}")
    print(f"Confusion Matrix:\n{cm}")
    print("-" * 40)

wine = load_wine()
X, y = wine.data, wine.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

run_pipeline(
    LogisticRegression(max_iter=10000, random_state=42),
    "Logistic Regression",
    X_train, X_test, y_train, y_test
)