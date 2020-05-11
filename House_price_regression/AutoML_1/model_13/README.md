# Summary of model_13

## Random Forest
- **criterion**: mae
- **max_features**: 0.7
- **min_samples_split**: 20
- **min_samples_leaf**: 18

## Validation
 - **validation_type**: kfold
 - **k_folds**: 5
 - **shuffle**: True

## Optimized metric
mse

## Training time

53.6 seconds

### Metric details:
| Metric   |     Score |
|:---------|----------:|
| MAE      |  3.00951  |
| MSE      | 23.9534   |
| RMSE     |  4.89423  |
| R2       |  0.713743 |



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