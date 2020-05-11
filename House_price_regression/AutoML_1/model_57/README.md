# Summary of model_57

## CatBoost
- **learning_rate**: 0.05
- **depth**: 7
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

27.8 seconds

### Metric details:
| Metric   |     Score |
|:---------|----------:|
| MAE      |  2.07913  |
| MSE      | 10.0902   |
| RMSE     |  3.17651  |
| R2       |  0.879417 |



## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)