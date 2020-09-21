import numpy as np
import pandas as pd
from supervised import AutoML

COLS = 10

for ROWS in [1000, 5000, 10000]:
    X = np.random.uniform(size=(ROWS, COLS))
    y = np.random.randint(0, 2, size=(ROWS,))

    automl = AutoML(results_path=f"AutoML_{ROWS//1000}k", mode="Explain", features_selection=True)
    automl.fit(X, y)
