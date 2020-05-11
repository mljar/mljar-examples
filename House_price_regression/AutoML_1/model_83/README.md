# Summary of model_83

## CatBoost
- **learning_rate**: 0.1
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

13.3 seconds

### Metric details:
| Metric   |     Score |
|:---------|----------:|
| MAE      |  2.14831  |
| MSE      | 10.5784   |
| RMSE     |  3.25244  |
| R2       |  0.873583 |



## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)