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
| logloss   | 0.693127 |   nan       |
| auc       | 0.5      |   nan       |
| f1        | 0.663816 |     0.44688 |
| accuracy  | 0.4968   |     0.44688 |
| precision | 0.4968   |     0.44688 |
| recall    | 1        |     0.44688 |
| mcc       | 0        |     0.44688 |


## Confusion matrix (at threshold=0.44688)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                       0 |                     629 |
| Labeled as positive |                       0 |                     621 |

## Learning curves
![Learning curves](learning_curves.png)