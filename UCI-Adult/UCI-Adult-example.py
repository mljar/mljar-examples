import os
import numpy as np
import pandas as pd
from mljar import Mljar

# please set MLJAR_TOKEN in your ENV
# export MLJAR_TOKEN=token_here
# or set it below
#os.environ["MLJAR_TOKEN"] = "*** your MLJAR_TOKEN goes here ***"

# Read dataset
# Dataset Adult. It is originally from from UCI repository (https://archive.ics.uci.edu/ml/index.html).
df = pd.read_csv('data/adult.csv', na_values='?', skipinitialspace=True)
# Show first lines of our dataset
df.head()

# First 14 columns will be input for classifier and the last one will be a target
input_cols = df.columns[:14]
target_col = df.columns[14]


# Let's define MLJAR project
mljar = Mljar(project='UCI-Adult',  # project's title that we will use to find it among our projects in MLJAR
              experiment='Try tree methods', # experiment's title
              validation_kfolds=5, # we will use 5-fold CV with stratify and shuffle
              validation_shuffle=True,
              validation_stratify=True,
              metric='auc', # we will use Area Under ROC Curve (AUC) as a metric,
              tuning_mode='Normal', # select tuning mode
              algorithms=['rfc', 'xgb', 'lgb'], # we want to tune Random Forest, LightGBM and Xgboost models
              create_ensemble=True, # create ensemble of all models,
              single_algorithm_time_limit=5 # time limit for single algorithm training in minutes
             )

# Run models prediction
mljar.fit(df[input_cols], df[target_col])

# Print out the most useful algorithm
print str(mljar.selected_algorithm)

# Run prediction on train dataset just for example
pred = mljar.predict(df[input_cols])

print 'Please go to your mljar account and check details of all models'
