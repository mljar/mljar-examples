# Summary of model_4

## Decision Tree
- **criterion**: entropy
- **max_depth**: 4

## Validation
 - **validation_type**: kfold
 - **k_folds**: 5
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

38.3 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.35068  |  nan        |
| auc       | 0.868882 |  nan        |
| f1        | 0.6373   |    0.33018  |
| accuracy  | 0.843289 |    0.485525 |
| precision | 0.980392 |    0.66254  |
| recall    | 0.999683 |    0        |
| mcc       | 0.536826 |    0.485525 |


## Confusion matrix (at threshold=0.33018)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                   14741 |                    5007 |
| Labeled as positive |                    1012 |                    5288 |

## Learning curves
![Learning curves](learning_curves.png)

## Tree visualizations

### Tree #1
![Tree 1](learner_1_tree.svg)
### Tree #2
![Tree 2](learner_2_tree.svg)
### Tree #3
![Tree 3](learner_3_tree.svg)
### Tree #4
![Tree 4](learner_4_tree.svg)
### Tree #5
![Tree 5](learner_5_tree.svg)

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