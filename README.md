# Examples how to use python AutoML package `mljar-supervised`

The MLJAR, Inc. provides python AutoML package [`mljar-supervised`](https://github.com/mljar/mljar-supervised) that is open-source with MIT license. Below are listed examples how it can be used.

- [**Income classification**](https://github.com/mljar/mljar-examples/tree/master/Income_classification) - it is a binary classification task on census data
- [**Iris classification**](https://github.com/mljar/mljar-examples/tree/master/Iris_classification) - it is a multiclass classification on Iris flowers data
- [**House price regression**](https://github.com/mljar/mljar-examples/tree/master/House_price_regression) - it is a regression task on Boston houses data


# Examples of using MLJAR.com with python REST API wrapper

[mljar.com](https://mljar.com) is a service for building Machine Learning models with simple User Interface available in the web browser. It can be also accessed with REST API below are examples how to use it.

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
