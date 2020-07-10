# Summary of 1_Baseline

## Baseline Classifier (Baseline)
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

0.0 seconds

### Metric details
|           |   setosa |   versicolor |   virginica |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------:|-------------:|------------:|-----------:|------------:|---------------:|----------:|
| precision |        0 |            0 |    0.352941 |   0.352941 |    0.117647 |       0.124567 |   1.09785 |
| recall    |        0 |            0 |    1        |   0.352941 |    0.333333 |       0.352941 |   1.09785 |
| f1-score  |        0 |            0 |    0.521739 |   0.352941 |    0.173913 |       0.184143 |   1.09785 |
| support   |       11 |           11 |   12        |   0.352941 |   34        |      34        |   1.09785 |


## Confusion matrix
|                       |   Predicted as setosa |   Predicted as versicolor |   Predicted as virginica |
|:----------------------|----------------------:|--------------------------:|-------------------------:|
| Labeled as setosa     |                     0 |                         0 |                       11 |
| Labeled as versicolor |                     0 |                         0 |                       11 |
| Labeled as virginica  |                     0 |                         0 |                       12 |

## Learning curves
![Learning curves](learning_curves.png)