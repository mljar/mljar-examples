# Summary of model_54

## CatBoost
- **learning_rate**: 0.05
- **depth**: 6
- **rsm**: 0.7
- **l2_leaf_reg**: 7
- **loss_function**: RMSE

## Validation
 - **validation_type**: kfold
 - **k_folds**: 5
 - **shuffle**: True

## Optimized metric
mse

## Training time

19.8 seconds

### Metric details:
| Metric   |     Score |
|:---------|----------:|
| MAE      |  2.14858  |
| MSE      | 10.1563   |
| RMSE     |  3.18689  |
| R2       |  0.878627 |



## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)