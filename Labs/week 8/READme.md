# Wine Classification ML Lab

A machine learning project using the Wine Dataset from scikit-learn.

---

## Dataset

The Wine dataset is built into scikit-learn. It contains 178 samples with
13 chemical features such as alcohol, malic acid, and ash. The goal is to
classify wines into one of three categories: class_0, class_1, or class_2.

---

## Parts Overview

### Part A - Dataset Preparation
Loads the Wine dataset and converts it into a Pandas DataFrame. Features are
assigned as column names and the target column is added. The data is then
split into training and testing sets using a 75/25 ratio with random_state=42
to ensure reproducibility.

### Part B - Model Training
Two models are trained on the dataset. A Logistic Regression model is trained
first and its predictions are stored. Then a KNN Classifier with k=5 is
trained and its predictions are compared with Logistic Regression.

### Part C - Model Evaluation
Accuracy scores are calculated for both models. A confusion matrix is
generated for Logistic Regression to identify true positives, false positives,
false negatives, and true negatives. A full classification report is also
printed showing precision, recall, and F1-score for each class.

### Part D - Model Improvement
The model is tested using one feature, then two features, and finally all 13
features to observe how more data improves accuracy. The train-test split is
also changed from 75/25 to 50/50 to see how a smaller training set affects
performance.

### Part E - Mini ML Pipeline
A complete pipeline that loads the dataset, splits the data, trains a Logistic
Regression model, makes predictions, and prints the accuracy score and
confusion matrix.

---

## Models Used

### Logistic Regression
Logistic Regression is a linear classifier that finds a decision boundary
between classes. It works by calculating the probability that a sample belongs
to a particular class using a sigmoid function. It is fast, easy to interpret,
and works well when the classes can be separated by a straight line or plane.

### K-Nearest Neighbors
KNN is a simple algorithm that classifies a new sample by looking at the k
closest training samples and taking a majority vote. It does not have a
training phase. However, it is sensitive to features that have very different
value ranges because it uses Euclidean distance to find neighbors.

### Decision Tree
A Decision Tree splits the data step by step based on feature values to
separate the classes. It is easy to understand and does not require feature
scaling. However, without any depth limit it can overfit the training data,
meaning it memorizes instead of learning general patterns.

---

## Comparison of Results

Logistic Regression achieved the highest accuracy of around 97.78 percent.
Decision Tree came second with around 91.11 percent accuracy. KNN performed
the lowest with around 77.78 percent accuracy. When features were reduced to
just one, accuracy dropped to around 55 percent, and using two features gave
around 64 percent. All 13 features gave the best result. Changing the split
to 50/50 slightly reduced accuracy from 97.78 to around 94.38 percent because
the model had less data to train on.

---

## Observation

Logistic Regression performed the best on this dataset because the Wine
classes are well separated and a linear boundary is enough to distinguish
them. KNN performed poorly because the 13 features have very different value
ranges. Features like proline have values in the hundreds while alcohol values
are between 11 and 15. This difference causes KNN to give too much importance
to features with large values when calculating distance. Scaling the features
using StandardScaler before training KNN would likely fix this and bring its
accuracy much closer to Logistic Regression.

---

