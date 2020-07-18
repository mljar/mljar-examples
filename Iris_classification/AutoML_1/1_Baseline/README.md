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

0.1 seconds

### Metric details
|           |   setosa |   versicolor |   virginica |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------:|-------------:|------------:|-----------:|------------:|---------------:|----------:|
| precision | 0.333333 |            0 |           0 |   0.333333 |    0.111111 |       0.111111 |   1.09861 |
| recall    | 1        |            0 |           0 |   0.333333 |    0.333333 |       0.333333 |   1.09861 |
| f1-score  | 0.5      |            0 |           0 |   0.333333 |    0.166667 |       0.166667 |   1.09861 |
| support   | 9        |            9 |           9 |   0.333333 |   27        |      27        |   1.09861 |


## Confusion matrix
|                       |   Predicted as setosa |   Predicted as versicolor |   Predicted as virginica |
|:----------------------|----------------------:|--------------------------:|-------------------------:|
| Labeled as setosa     |                     9 |                         0 |                        0 |
| Labeled as versicolor |                     9 |                         0 |                        0 |
| Labeled as virginica  |                     9 |                         0 |                        0 |

## Learning curves
![Learning curves](learning_curves.png)