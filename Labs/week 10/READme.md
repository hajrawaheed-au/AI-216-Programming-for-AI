# AI-216 Programming for Artificial Intelligence
## Lab 10: End-to-End AI Project Implementation

# Project Structure

This project follows a modular structure:

project/
├── data/
├── preprocessing.py
├── train.py
├── evaluate.py
├── predict.py
├── main.py
└── README.md

## Module Explanation

### preprocessing.py

- Loads Wine dataset
- Converts dataset into DataFrame
- Separates features and target values

### train.py

- Splits dataset
- Trains machine learning model
- Returns trained model and testing data

### evaluate.py

- Calculates:
  - Accuracy
  - Confusion Matrix
  - Classification Report

### predict.py

- Saves model using joblib
- Loads saved model
- Predicts new samples

### main.py

Controls complete system workflow.

Steps:

1. Load dataset
2. Train model
3. Evaluate model
4. Save model
5. Reload model
6. Predict sample

## Model Used

Logistic Regression

## Evaluation Results

The model produced high accuracy on the Wine dataset with good classification performance.

## Improvement Suggestion

Apply feature scaling using StandardScaler and compare results with additional models such as:

- KNN
- Decision Tree
- Random Forest

This may further improve model performance.

## Conclusion

This lab demonstrates a complete AI system using modular programming and machine learning workflow.