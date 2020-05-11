# Summary of model_58

## CatBoost
- **learning_rate**: 0.1
- **depth**: 6
- **rsm**: 0.6
- **l2_leaf_reg**: 7
- **loss_function**: RMSE

## Validation
 - **validation_type**: kfold
 - **k_folds**: 5
 - **shuffle**: True

## Optimized metric
mse

## Training time

44.0 seconds

### Metric details:
| Metric   |     Score |
|:---------|----------:|
| MAE      |  2.16617  |
| MSE      | 10.4178   |
| RMSE     |  3.22766  |
| R2       |  0.875502 |



## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)