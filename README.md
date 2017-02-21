# Examples of using MLJAR python API

Examples how MLJAR python API can be used for building machine learning models:

 - **auto-trading-numerai** is an example of stock market prediction based on raw data from Numer.ai.
 It is a task of building binary classifier. In the example we run Xgboost, LightGBM and Neural Network models.
 - **UCI-Adult** is an example of model which predicts whether income exceeds $50K/yr based on census data.
 It is a task of binary classification. In the example we run Random Forest, LightGBM and Xgboost models.

## What's going on?

 1. In this examples you load example datasets and build machine learning models with MLJAR.
 2. To build models with MLJAR you are using our super easy [python API][1].
 3. MLJAR will check for you many machine learning algorithms, tune each of algorithm and create an ensemble.
 4. You can view details of your models on [MLJAR][2] website after login to your account.

[1]: https://github.com/mljar/mljar-api-python
[2]: https://mljar.com
