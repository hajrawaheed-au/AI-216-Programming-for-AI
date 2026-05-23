import pandas as pd
from sklearn.datasets import load_wine


def load_data():

    wine = load_wine()

    X = pd.DataFrame(
        wine.data,
        columns=wine.feature_names
    )

    y = wine.target

    return X, y