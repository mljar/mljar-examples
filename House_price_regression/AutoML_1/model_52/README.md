# Summary of model_52

## CatBoost
- **learning_rate**: 0.2
- **depth**: 8
- **rsm**: 1.0
- **l2_leaf_reg**: 1
- **loss_function**: MAE

## Validation
 - **validation_type**: kfold
 - **k_folds**: 5
 - **shuffle**: True

## Optimized metric
mse

## Training time

7.4 seconds

### Metric details:
| Metric   |    Score |
|:---------|---------:|
| MAE      |  2.55178 |
| MSE      | 16.657   |
| RMSE     |  4.0813  |
| R2       |  0.80094 |



## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)