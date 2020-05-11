# Summary of model_55

## CatBoost
- **learning_rate**: 0.05
- **depth**: 6
- **rsm**: 0.9
- **l2_leaf_reg**: 5
- **loss_function**: RMSE

## Validation
 - **validation_type**: kfold
 - **k_folds**: 5
 - **shuffle**: True

## Optimized metric
mse

## Training time

24.0 seconds

### Metric details:
| Metric   |   Score |
|:---------|--------:|
| MAE      | 2.10716 |
| MSE      | 9.83549 |
| RMSE     | 3.13616 |
| R2       | 0.88246 |



## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)