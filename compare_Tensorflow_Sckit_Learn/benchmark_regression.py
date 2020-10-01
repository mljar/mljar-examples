import numpy as np
import pandas as pd
from supervised.automl import AutoML
from sklearn.model_selection import train_test_split
import os
import time
import json
from sklearn.metrics import log_loss, mean_squared_error

from sklearn.model_selection import train_test_split
from pmlb import fetch_data, regression_dataset_names

results = json.load(open("results_regression.json"))

for dataset in regression_dataset_names:

    X, y = fetch_data(dataset, return_X_y=True)

    if X.shape[0] < 1000:
        continue
    if dataset in [r["dataset"] for r in results]:
        continue
    print(dataset, X.shape, y[:5], np.unique(y))

    train_X, test_X, train_y, test_y = train_test_split(
        X, y, test_size=0.25, random_state=12
    )

    mlp = AutoML(
        algorithms=["MLP"],
        mode="Perform",
        explain_level=0,
        train_ensemble=False,
        golden_features=False,
        features_selection=False,
        ml_task="regression",
    )
    nn = AutoML(
        algorithms=["Neural Network"],
        mode="Perform",
        explain_level=0,
        train_ensemble=False,
        golden_features=False,
        features_selection=False,
        ml_task="regression",
    )

    mlp.fit(train_X, train_y)
    mlp_time = np.round(time.time() - mlp._start_time, 2)
    nn.fit(train_X, train_y)
    nn_time = np.round(time.time() - nn._start_time, 2)

    mlp_mse = mean_squared_error(test_y, mlp.predict(test_X))
    nn_mse = mean_squared_error(test_y, nn.predict(test_X))

    print(dataset, X.shape, np.unique(y), mlp_mse, nn_mse)

    results += [
        {
            "dataset": dataset,
            "nrows": X.shape[0],
            "ncols": X.shape[1],
            "mlp_mse": mlp_mse,
            "nn_mse": nn_mse,
            "mlp_time": mlp_time,
            "nn_time": nn_time,
        }
    ]

    with open("results_regression.json", "w") as fout:
        fout.write(json.dumps(results, indent=4))

