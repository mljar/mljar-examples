# Summary of model_5

## Decision Tree
- **criterion**: entropy
- **max_depth**: 1

## Validation
 - **validation_type**: kfold
 - **k_folds**: 5
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

25.7 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.470718 | nan         |
| auc       | 0.729698 | nan         |
| f1        | 0.565739 |   0.273742  |
| accuracy  | 0.748464 |   0.451526  |
| precision | 0.450626 |   0.273742  |
| recall    | 1        |   0.0875609 |
| mcc       | 0.404586 |   0.273742  |


## Confusion matrix (at threshold=0.273742)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                   13912 |                    5836 |
| Labeled as positive |                    1513 |                    4787 |

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