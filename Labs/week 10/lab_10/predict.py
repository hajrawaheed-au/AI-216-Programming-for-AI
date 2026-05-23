import joblib


def save_model(model):

    joblib.dump(
        model,
        "wine_model.pkl"
    )

    print("Model saved successfully")


def load_model():

    model = joblib.load(
        "wine_model.pkl"
    )

    return model


def predict_sample(model, sample):

    prediction = model.predict(
        [sample]
    )

    return prediction