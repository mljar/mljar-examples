# Summary of model_81

## CatBoost
- **learning_rate**: 0.1
- **depth**: 7
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

11.0 seconds

### Metric details:
| Metric   |     Score |
|:---------|----------:|
| MAE      |  2.17444  |
| MSE      | 10.9733   |
| RMSE     |  3.3126   |
| R2       |  0.868862 |



## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)