import os
import time
import json
import numpy as np
import pandas as pd
from supervised.automl import AutoML
from sklearn.model_selection import train_test_split
from sklearn.metrics import log_loss

from sklearn.model_selection import train_test_split
from pmlb import fetch_data, classification_dataset_names

results = json.load(open("results.json"))

for classification_dataset in classification_dataset_names:

    X, y = fetch_data(classification_dataset, return_X_y=True)
    if X.shape[0] < 1000:
        continue
    if classification_dataset in [r["dataset"] for r in results]:
        continue
    print(classification_dataset, X.shape, y[:5], np.unique(y))

    train_X, test_X, train_y, test_y = train_test_split(
        X, y, test_size=0.25, stratify=y, random_state=12
    )
    ml_task = "binary_classification"
    if len(np.unique(y)) > 2:
        ml_task = "multiclass_classification"

    mlp = AutoML(
        algorithms=["MLP"],
        mode="Perform",
        explain_level=0,
        train_ensemble=False,
        golden_features=False,
        features_selection=False,
        ml_task=ml_task,
    )
    nn = AutoML(
        algorithms=["Neural Network"],
        mode="Perform",
        explain_level=0,
        train_ensemble=False,
        golden_features=False,
        features_selection=False,
        ml_task=ml_task,
    )

    mlp.fit(train_X, train_y)
    mlp_time = np.round(time.time() - mlp._start_time, 2)
    nn.fit(train_X, train_y)
    nn_time = np.round(time.time() - nn._start_time, 2)

    mlp_ll = log_loss(test_y, mlp.predict_proba(test_X))
    nn_ll = log_loss(test_y, nn.predict_proba(test_X))

    print(classification_dataset, X.shape, np.unique(y), mlp_ll, nn_ll)

    results += [
        {
            "dataset": classification_dataset,
            "nrows": X.shape[0],
            "ncols": X.shape[1],
            "n_classes": len(np.unique(y)),
            "mlp_logloss": mlp_ll,
            "nn_logloss": nn_ll,
            "mlp_time": mlp_time,
            "nn_time": nn_time,
        }
    ]

    with open("results.json", "w") as fout:
        fout.write(json.dumps(results, indent=4))
