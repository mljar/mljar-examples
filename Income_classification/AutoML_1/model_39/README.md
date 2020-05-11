# Summary of model_39

## Extreme Gradient Boosting (Xgboost)
- **objective**: binary:logistic
- **eval_metric**: auc
- **eta**: 0.075
- **max_depth**: 3
- **min_child_weight**: 7
- **subsample**: 0.3
- **colsample_bytree**: 0.7

## Validation
 - **validation_type**: kfold
 - **k_folds**: 5
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

45.4 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.296138 | nan           |
| auc       | 0.918678 | nan           |
| f1        | 0.713635 |   0.360524    |
| accuracy  | 0.864366 |   0.514423    |
| precision | 0.964286 |   0.85817     |
| recall    | 1        |   0.000106003 |
| mcc       | 0.61716  |   0.418399    |


## Confusion matrix (at threshold=0.360524)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                   17430 |                    2318 |
| Labeled as positive |                    1519 |                    4781 |

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

### Top-10 Worst decisions for class 0 (Fold #1)
![SHAP worst decisions class 0 from fold 1](learner_1_shap_class_0_worst_decisions.png)
### Top-10 Worst decisions for class 0 (Fold #2)
![SHAP worst decisions class 0 from fold 2](learner_2_shap_class_0_worst_decisions.png)
### Top-10 Worst decisions for class 0 (Fold #3)
![SHAP worst decisions class 0 from fold 3](learner_3_shap_class_0_worst_decisions.png)
### Top-10 Worst decisions for class 0 (Fold #4)
![SHAP worst decisions class 0 from fold 4](learner_4_shap_class_0_worst_decisions.png)
### Top-10 Worst decisions for class 0 (Fold #5)
![SHAP worst decisions class 0 from fold 5](learner_5_shap_class_0_worst_decisions.png)
### Top-10 Best decisions for class 0 (Fold #1)
![SHAP best decisions class 0 from fold 1](learner_1_shap_class_0_best_decisions.png)
### Top-10 Best decisions for class 0 (Fold #2)
![SHAP best decisions class 0 from fold 2](learner_2_shap_class_0_best_decisions.png)
### Top-10 Best decisions for class 0 (Fold #3)
![SHAP best decisions class 0 from fold 3](learner_3_shap_class_0_best_decisions.png)
### Top-10 Best decisions for class 0 (Fold #4)
![SHAP best decisions class 0 from fold 4](learner_4_shap_class_0_best_decisions.png)
### Top-10 Best decisions for class 0 (Fold #5)
![SHAP best decisions class 0 from fold 5](learner_5_shap_class_0_best_decisions.png)
### Top-10 Worst decisions for class 1 (Fold #1)
![SHAP worst decisions class 1 from fold 1](learner_1_shap_class_1_worst_decisions.png)
### Top-10 Worst decisions for class 1 (Fold #2)
![SHAP worst decisions class 1 from fold 2](learner_2_shap_class_1_worst_decisions.png)
### Top-10 Worst decisions for class 1 (Fold #3)
![SHAP worst decisions class 1 from fold 3](learner_3_shap_class_1_worst_decisions.png)
### Top-10 Worst decisions for class 1 (Fold #4)
![SHAP worst decisions class 1 from fold 4](learner_4_shap_class_1_worst_decisions.png)
### Top-10 Worst decisions for class 1 (Fold #5)
![SHAP worst decisions class 1 from fold 5](learner_5_shap_class_1_worst_decisions.png)
### Top-10 Best decisions for class 1 (Fold #1)
![SHAP best decisions class 1 from fold 1](learner_1_shap_class_1_best_decisions.png)
### Top-10 Best decisions for class 1 (Fold #2)
![SHAP best decisions class 1 from fold 2](learner_2_shap_class_1_best_decisions.png)
### Top-10 Best decisions for class 1 (Fold #3)
![SHAP best decisions class 1 from fold 3](learner_3_shap_class_1_best_decisions.png)
### Top-10 Best decisions for class 1 (Fold #4)
![SHAP best decisions class 1 from fold 4](learner_4_shap_class_1_best_decisions.png)
### Top-10 Best decisions for class 1 (Fold #5)
![SHAP best decisions class 1 from fold 5](learner_5_shap_class_1_best_decisions.png)