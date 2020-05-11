# Summary of model_71

## Random Forest
- **criterion**: mae
- **max_features**: 0.7
- **min_samples_split**: 2
- **min_samples_leaf**: 1

## Validation
 - **validation_type**: kfold
 - **k_folds**: 5
 - **shuffle**: True

## Optimized metric
mse

## Training time

75.6 seconds

### Metric details:
| Metric   |     Score |
|:---------|----------:|
| MAE      |  2.34351  |
| MSE      | 12.6593   |
| RMSE     |  3.55799  |
| R2       |  0.848715 |



## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)

## SHAP Importance
![SHAP Importance](shap_importance.png)

## SHAP Dependence plots

### Dependence (Fold #1)
![SHAP Dependence from fold 1](learner_1_shap_dependence.png)
### Dependence (Fold #2)
![SHAP Dependence from fold 2](learner_2_shap_dependence.png)
### Dependence (Fold #3)
![SHAP Dependence from fold 3](learner_3_shap_dependence.png)
### Dependence (Fold #4)
![SHAP Dependence from fold 4](learner_4_shap_dependence.png)
### Dependence (Fold #5)
![SHAP Dependence from fold 5](learner_5_shap_dependence.png)

## SHAP Decision plots

### Top-10 Worst decisions (Fold #1)
![SHAP worst decisions from fold 1](learner_1_shap_worst_decisions.png)
### Top-10 Worst decisions (Fold #2)
![SHAP worst decisions from fold 2](learner_2_shap_worst_decisions.png)
### Top-10 Worst decisions (Fold #3)
![SHAP worst decisions from fold 3](learner_3_shap_worst_decisions.png)
### Top-10 Worst decisions (Fold #4)
![SHAP worst decisions from fold 4](learner_4_shap_worst_decisions.png)
### Top-10 Worst decisions (Fold #5)
![SHAP worst decisions from fold 5](learner_5_shap_worst_decisions.png)
### Top-10 Best decisions (Fold #1)
![SHAP best decisions from fold 1](learner_1_shap_best_decisions.png)
### Top-10 Best decisions (Fold #2)
![SHAP best decisions from fold 2](learner_2_shap_best_decisions.png)
### Top-10 Best decisions (Fold #3)
![SHAP best decisions from fold 3](learner_3_shap_best_decisions.png)
### Top-10 Best decisions (Fold #4)
![SHAP best decisions from fold 4](learner_4_shap_best_decisions.png)
### Top-10 Best decisions (Fold #5)
![SHAP best decisions from fold 5](learner_5_shap_best_decisions.png)