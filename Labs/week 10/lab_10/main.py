from preprocessing import load_data
from train import train_model
from evaluate import evaluate_model
from predict import save_model
from predict import load_model
from predict import predict_sample


print("\nLoading dataset...")
X, y = load_data()


print("\nTraining model...")
model, X_test, y_test = train_model(
    X,
    y
)


print("\nEvaluating model...")
evaluate_model(
    model,
    X_test,
    y_test
)


print("\nSaving model...")
save_model(model)


print("\nLoading saved model...")
loaded_model = load_model()


print("\nTesting prediction on one sample...")

sample = X.iloc[0].values

prediction = predict_sample(
    loaded_model,
    sample
)

print(
    "Predicted Class:",
    prediction[0]
)