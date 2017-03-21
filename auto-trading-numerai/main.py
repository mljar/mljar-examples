'''
Example how to make auto-trading script on Numer.ai data.
It is using MLJAR for model training.
'''
import os
import pandas as pd
import numerapi # API to interact with Numer.ai
from mljar import Mljar # API to build model

# your credentials from numer.ai
NUMERAI_USER = '######your mail#######'
NUMERAI_PASS = '######your pass#######'
# files with Numer.ai data
TRAIN_FNAME = './numerai_training_data.csv'
TEST_FNAME = './numerai_tournament_data.csv'
# file with our predictions
PREDICTIONS_FNAME = './mljar-prediction-raw-data.csv'

def some_tricky_unsupervised_preprocessing(X_train, X_test):
    # do some magic here
    return X_train, X_test

def main():
    # login to numerai to get token
    print 'Login into Numer.ai'
    api = numerapi.NumerAPI(NUMERAI_USER, NUMERAI_PASS)
    # get datasets
    print 'Get dataset'
    if not os.path.isfile(TRAIN_FNAME):
        api.download_current_dataset(dest_path='.', unzip=True)
    # read datasets
    train = pd.read_csv(TRAIN_FNAME)
    test  = pd.read_csv(TEST_FNAME)
    print 'Numer.ai data downloaded'
    print 'Train shape', train.shape, 'test shape', test.shape

    X_train = train[train.columns[:50]]
    y_train = train['target']
    X_test = test

    print 'Create MLJAR project and experiment'
    models = Mljar(project='Auto-trading', experiment="Raw data",
                    metric='logloss',
                    validation_kfolds=5, # we will use 5-fold CV with stratify and shuffle
                    validation_shuffle=True,
                    validation_stratify=True,
                    algorithms=['xgb', 'lgb', 'mlp'], # select Xgboost, LightGBM and Neural Network
                    tuning_mode='Normal', # number of models to be checked for each algorithm
                    single_algorithm_time_limit=5) # 5 minutes for training single model

    print 'Train models:'
    # fit models - that's all, only one line of code ;)
    models.fit(X_train, y_train)
    # get predictions on test data
    predictions = models.predict(X_test)
    # save predictions to file
    predictions.to_csv(PREDICTIONS_FNAME, index=False)
    result = api.upload_prediction(PREDICTIONS_FNAME)
    print 'Your score:', result['submission']['accuracy_score']


if __name__=="__main__":
    main()
