# Summary of 1_Baseline

## Baseline Classifier (Baseline)
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

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.693055 |   nan       |
| auc       | 0.5      |   nan       |
| f1        | 0.660595 |     0.44364 |
| accuracy  | 0.4932   |     0.44364 |
| precision | 0.4932   |     0.44364 |
| recall    | 1        |     0.44364 |
| mcc       | 0        |     0.44364 |


## Confusion matrix (at threshold=0.44364)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                       0 |                    1267 |
| Labeled as positive |                       0 |                    1233 |

## Learning curves
![Learning curves](learning_curves.png)