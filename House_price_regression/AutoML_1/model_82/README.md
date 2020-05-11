# Summary of model_82

## CatBoost
- **learning_rate**: 0.01
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

42.4 seconds

### Metric details:
| Metric   |     Score |
|:---------|----------:|
| MAE      |  2.20872  |
| MSE      | 11.3846   |
| RMSE     |  3.37411  |
| R2       |  0.863948 |



## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)