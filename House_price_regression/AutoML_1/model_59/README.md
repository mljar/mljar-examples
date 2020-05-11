# Summary of model_59

## CatBoost
- **learning_rate**: 0.05
- **depth**: 6
- **rsm**: 0.7
- **l2_leaf_reg**: 5
- **loss_function**: RMSE

## Validation
 - **validation_type**: kfold
 - **k_folds**: 5
 - **shuffle**: True

## Optimized metric
mse

## Training time

43.6 seconds

### Metric details:
| Metric   |     Score |
|:---------|----------:|
| MAE      |  2.19994  |
| MSE      | 10.7742   |
| RMSE     |  3.28241  |
| R2       |  0.871242 |



## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)