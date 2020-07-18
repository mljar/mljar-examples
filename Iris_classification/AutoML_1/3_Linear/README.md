# Summary of 3_Linear

## Logistic Regression (Linear)
- **num_class**: 3
- **explain_level**: 2

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.75
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

27.1 seconds

### Metric details
|           |   setosa |   versicolor |   virginica |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------:|-------------:|------------:|-----------:|------------:|---------------:|----------:|
| precision |        1 |            1 |           1 |          1 |           1 |              1 |   0.12529 |
| recall    |        1 |            1 |           1 |          1 |           1 |              1 |   0.12529 |
| f1-score  |        1 |            1 |           1 |          1 |           1 |              1 |   0.12529 |
| support   |        9 |            9 |           9 |          1 |          27 |             27 |   0.12529 |


## Confusion matrix
|                       |   Predicted as setosa |   Predicted as versicolor |   Predicted as virginica |
|:----------------------|----------------------:|--------------------------:|-------------------------:|
| Labeled as setosa     |                     9 |                         0 |                        0 |
| Labeled as versicolor |                     0 |                         9 |                        0 |
| Labeled as virginica  |                     0 |                         0 |                        9 |

## Learning curves
![Learning curves](learning_curves.png)

## Coefficients

### Coefficients learner #1
|                   |    setosa |   versicolor |   virginica |
|:------------------|----------:|-------------:|------------:|
| intercept         | -0.340419 |   1.61125    |   -1.27083  |
| sepal length (cm) | -1.03992  |   0.500877   |    0.539043 |
| sepal width (cm)  |  0.840776 |  -0.382739   |   -0.458037 |
| petal length (cm) | -1.55192  |   0.00792678 |    1.544    |
| petal width (cm)  | -1.37221  |  -0.835489   |    2.2077   |


## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)

## SHAP Importance
![SHAP Importance](shap_importance.png)

## SHAP Dependence plots

### Dependence setosa (Fold #1)
![SHAP Dependence from fold 1](learner_1_shap_dependence_class_setosa.png)
### Dependence versicolor (Fold #1)
![SHAP Dependence from fold 1](learner_1_shap_dependence_class_versicolor.png)
### Dependence virginica (Fold #1)
![SHAP Dependence from fold 1](learner_1_shap_dependence_class_virginica.png)

## SHAP Decision plots

### Worst decisions for selected sample #1 (Fold #1)
![SHAP worst decisions from fold 1](learner_1_sample_0_worst_decisions.png)
### Worst decisions for selected sample #2 (Fold #1)
![SHAP worst decisions from fold 1](learner_1_sample_1_worst_decisions.png)
### Worst decisions for selected sample #3 (Fold #1)
![SHAP worst decisions from fold 1](learner_1_sample_2_worst_decisions.png)
### Worst decisions for selected sample #4 (Fold #1)
![SHAP worst decisions from fold 1](learner_1_sample_3_worst_decisions.png)
### Best decisions for selected sample #1 (Fold #1)
![SHAP best decisions from fold 1](learner_1_sample_0_best_decisions.png)
### Best decisions for selected sample #2 (Fold #1)
![SHAP best decisions from fold 1](learner_1_sample_1_best_decisions.png)
### Best decisions for selected sample #3 (Fold #1)
![SHAP best decisions from fold 1](learner_1_sample_2_best_decisions.png)
### Best decisions for selected sample #4 (Fold #1)
![SHAP best decisions from fold 1](learner_1_sample_3_best_decisions.png)