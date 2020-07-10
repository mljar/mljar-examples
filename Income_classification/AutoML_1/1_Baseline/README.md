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

0.1 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.551985 |  nan        |
| auc       | 0.5      |  nan        |
| f1        | 0.388119 |    0.216615 |
| accuracy  | 0.240786 |    0.216615 |
| precision | 0.240786 |    0.216615 |
| recall    | 1        |    0.216615 |
| mcc       | 0        |    0.216615 |


## Confusion matrix (at threshold=0.216615)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                       0 |                    4944 |
| Labeled as positive |                       0 |                    1568 |

## Learning curves
![Learning curves](learning_curves.png)