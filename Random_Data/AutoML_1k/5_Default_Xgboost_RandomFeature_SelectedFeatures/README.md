# Summary of 5_Default_Xgboost_RandomFeature_SelectedFeatures

## Extreme Gradient Boosting (Xgboost)
- **objective**: binary:logistic
- **eval_metric**: logloss
- **eta**: 0.1
- **max_depth**: 6
- **min_child_weight**: 1
- **subsample**: 1.0
- **colsample_bytree**: 1.0
- **explain_level**: 1

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.75
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

0.7 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.686194 |  nan        |
| auc       | 0.571241 |  nan        |
| f1        | 0.680739 |    0.340714 |
| accuracy  | 0.576    |    0.483601 |
| precision | 0.625    |    0.578755 |
| recall    | 1        |    0.340714 |
| mcc       | 0.151957 |    0.475795 |


## Confusion matrix (at threshold=0.483601)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                       0 |                     121 |
| Labeled as positive |                       0 |                     129 |

## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)