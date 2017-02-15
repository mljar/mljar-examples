import os
import numpy as np
import pandas as pd
from mljar import Mljar

os.environ["MLJAR_TOKEN"] = "*** your MLJAR_TOKEN goes here ***"
# Dataset Adult. It is originally from from UCI repository (https://archive.ics.uci.edu/ml/index.html).
df = pd.read_csv('data/adult.csv', na_values='?', skipinitialspace=True)
# Show first lines of our dataset
df.head()

# First 14 columns will be input for classifier and the last one will be a target
input_cols = df.columns[:14]
target_col = df.columns[14]

# Let's define MLJAR project
mljar = Mljar(project='UCI-Adult',  # project's title that we will use to find it among our projects in MLJAR
              experiment='First try', # experiment's title
              validation='5fold', # we will use 5-fold CV
              metric='auc', # we will use Area Under ROC Curve (AUC) as a metric,
              tuning_mode='Normal', # select tuning mode
              algorithms=['rfc'], # we want to tune Random Forest and Nueral Network models
              create_ensemble=True, # create ensemble of all models,
              single_algorithm_time_limit=1 # time limit for single algorithm training
             )
# run models prediction
mljar.fit(df[input_cols], df[target_col])

# print out the most useful algorithm
mljar.selected_algorithm.show()

# run prediction
pred = mljar.predict(df[input_cols])
