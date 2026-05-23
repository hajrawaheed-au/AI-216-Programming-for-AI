from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report


def evaluate_model(model, X_test, y_test):

    predictions = model.predict(X_test)

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    print("\nAccuracy:")
    print(accuracy)

    print("\nConfusion Matrix:")
    print(confusion_matrix(
        y_test,
        predictions
    ))

    print("\nClassification Report:")
    print(classification_report(
        y_test,
        predictions
    ))