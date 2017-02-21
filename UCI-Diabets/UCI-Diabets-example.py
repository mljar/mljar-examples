import os
import numpy as np
import pandas as pd
from sklearn import datasets
from mljar import Mljar
from mljar.client.dataset import DatasetClient

os.environ["MLJAR_TOKEN"] = "*** your MLJAR_TOKEN ***"

diabetes = datasets.load_diabetes()
X = diabetes.data
y = diabetes.target

# Let's define MLJAR project
mljar = Mljar(project='UCI-Diabets',  # project's title that we will use to find it among our projects in MLJAR
              experiment='First try', # experiment's title
              validation='5fold', # we will use 5-fold CV
              metric='rmse', # we will use Area Under ROC Curve (AUC) as a metric,
              tuning_mode='Normal', # select tuning mode
              algorithms=['rfr'], # we want to tune Random Forest and Nueral Network models
              create_ensemble=True, # create ensemble of all models,
              single_algorithm_time_limit=1 # time limit for single algorithm training
             )

mljar.fit(X, y)

print 'Selected algorithm'
mljar.selected_algorithm.show()

#pred = mljar.predict(df[input_cols])
#print pred.shape
