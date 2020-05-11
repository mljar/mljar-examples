# Summary of model_47

## CatBoost
- **learning_rate**: 0.1
- **depth**: 6
- **rsm**: 0.5
- **l2_leaf_reg**: 7
- **loss_function**: RMSE

## Validation
 - **validation_type**: kfold
 - **k_folds**: 5
 - **shuffle**: True

## Optimized metric
mse

## Training time

12.0 seconds

### Metric details:
| Metric   |   Score |
|:---------|--------:|
| MAE      | 2.07849 |
| MSE      | 9.89328 |
| RMSE     | 3.14536 |
| R2       | 0.88177 |



## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)