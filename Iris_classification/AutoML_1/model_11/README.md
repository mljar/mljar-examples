# Summary of model_11

## Random Forest
- **criterion**: gini
- **max_features**: 0.7
- **min_samples_split**: 2
- **min_samples_leaf**: 1
- **num_class**: 3

## Validation
 - **validation_type**: kfold
 - **k_folds**: 5
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

28.7 seconds

### Metric details
|           |   setosa |   versicolor |   virginica |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------:|-------------:|------------:|-----------:|------------:|---------------:|----------:|
| precision |        1 |     0.930233 |    0.934783 |   0.955556 |    0.955005 |       0.955556 |  0.118912 |
| recall    |        1 |     0.930233 |    0.934783 |   0.955556 |    0.955005 |       0.955556 |  0.118912 |
| f1-score  |        1 |     0.930233 |    0.934783 |   0.955556 |    0.955005 |       0.955556 |  0.118912 |
| support   |       46 |    43        |   46        |   0.955556 |  135        |     135        |  0.118912 |


## Confusion matrix
|                       |   Predicted as setosa |   Predicted as versicolor |   Predicted as virginica |
|:----------------------|----------------------:|--------------------------:|-------------------------:|
| Labeled as setosa     |                    46 |                         0 |                        0 |
| Labeled as versicolor |                     0 |                        40 |                        3 |
| Labeled as virginica  |                     0 |                         3 |                       43 |

## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)

## SHAP Importance
![SHAP Importance](shap_importance.png)

## SHAP Dependence plots

### Dependence setosa (Fold #1)
![SHAP Dependence from fold 1](learner_1_shap_dependence_class_setosa.png)
### Dependence versicolor (Fold #1)
![SHAP Dependence from fold 1](learner_1_shap_dependence_class_versicolor.png)
### Dependence virginica (Fold #1)
![SHAP Dependence from fold 1](learner_1_shap_dependence_class_virginica.png)
### Dependence setosa (Fold #2)
![SHAP Dependence from fold 2](learner_2_shap_dependence_class_setosa.png)
### Dependence versicolor (Fold #2)
![SHAP Dependence from fold 2](learner_2_shap_dependence_class_versicolor.png)
### Dependence virginica (Fold #2)
![SHAP Dependence from fold 2](learner_2_shap_dependence_class_virginica.png)
### Dependence setosa (Fold #3)
![SHAP Dependence from fold 3](learner_3_shap_dependence_class_setosa.png)
### Dependence versicolor (Fold #3)
![SHAP Dependence from fold 3](learner_3_shap_dependence_class_versicolor.png)
### Dependence virginica (Fold #3)
![SHAP Dependence from fold 3](learner_3_shap_dependence_class_virginica.png)
### Dependence setosa (Fold #4)
![SHAP Dependence from fold 4](learner_4_shap_dependence_class_setosa.png)
### Dependence versicolor (Fold #4)
![SHAP Dependence from fold 4](learner_4_shap_dependence_class_versicolor.png)
### Dependence virginica (Fold #4)
![SHAP Dependence from fold 4](learner_4_shap_dependence_class_virginica.png)
### Dependence setosa (Fold #5)
![SHAP Dependence from fold 5](learner_5_shap_dependence_class_setosa.png)
### Dependence versicolor (Fold #5)
![SHAP Dependence from fold 5](learner_5_shap_dependence_class_versicolor.png)
### Dependence virginica (Fold #5)
![SHAP Dependence from fold 5](learner_5_shap_dependence_class_virginica.png)

## SHAP Decision plots

### Worst decisions for selected sample #1 (Fold #1)
![SHAP worst decisions from fold 1](learner_1_sample_0_worst_decisions.png)
### Worst decisions for selected sample #1 (Fold #2)
![SHAP worst decisions from fold 2](learner_2_sample_0_worst_decisions.png)
### Worst decisions for selected sample #1 (Fold #3)
![SHAP worst decisions from fold 3](learner_3_sample_0_worst_decisions.png)
### Worst decisions for selected sample #1 (Fold #4)
![SHAP worst decisions from fold 4](learner_4_sample_0_worst_decisions.png)
### Worst decisions for selected sample #1 (Fold #5)
![SHAP worst decisions from fold 5](learner_5_sample_0_worst_decisions.png)
### Worst decisions for selected sample #2 (Fold #1)
![SHAP worst decisions from fold 1](learner_1_sample_1_worst_decisions.png)
### Worst decisions for selected sample #2 (Fold #2)
![SHAP worst decisions from fold 2](learner_2_sample_1_worst_decisions.png)
### Worst decisions for selected sample #2 (Fold #3)
![SHAP worst decisions from fold 3](learner_3_sample_1_worst_decisions.png)
### Worst decisions for selected sample #2 (Fold #4)
![SHAP worst decisions from fold 4](learner_4_sample_1_worst_decisions.png)
### Worst decisions for selected sample #2 (Fold #5)
![SHAP worst decisions from fold 5](learner_5_sample_1_worst_decisions.png)
### Worst decisions for selected sample #3 (Fold #1)
![SHAP worst decisions from fold 1](learner_1_sample_2_worst_decisions.png)
### Worst decisions for selected sample #3 (Fold #2)
![SHAP worst decisions from fold 2](learner_2_sample_2_worst_decisions.png)
### Worst decisions for selected sample #3 (Fold #3)
![SHAP worst decisions from fold 3](learner_3_sample_2_worst_decisions.png)
### Worst decisions for selected sample #3 (Fold #4)
![SHAP worst decisions from fold 4](learner_4_sample_2_worst_decisions.png)
### Worst decisions for selected sample #3 (Fold #5)
![SHAP worst decisions from fold 5](learner_5_sample_2_worst_decisions.png)
### Worst decisions for selected sample #4 (Fold #1)
![SHAP worst decisions from fold 1](learner_1_sample_3_worst_decisions.png)
### Worst decisions for selected sample #4 (Fold #2)
![SHAP worst decisions from fold 2](learner_2_sample_3_worst_decisions.png)
### Worst decisions for selected sample #4 (Fold #3)
![SHAP worst decisions from fold 3](learner_3_sample_3_worst_decisions.png)
### Worst decisions for selected sample #4 (Fold #4)
![SHAP worst decisions from fold 4](learner_4_sample_3_worst_decisions.png)
### Worst decisions for selected sample #4 (Fold #5)
![SHAP worst decisions from fold 5](learner_5_sample_3_worst_decisions.png)
### Best decisions for selected sample #1 (Fold #1)
![SHAP best decisions from fold 1](learner_1_sample_0_best_decisions.png)
### Best decisions for selected sample #1 (Fold #2)
![SHAP best decisions from fold 2](learner_2_sample_0_best_decisions.png)
### Best decisions for selected sample #1 (Fold #3)
![SHAP best decisions from fold 3](learner_3_sample_0_best_decisions.png)
### Best decisions for selected sample #1 (Fold #4)
![SHAP best decisions from fold 4](learner_4_sample_0_best_decisions.png)
### Best decisions for selected sample #1 (Fold #5)
![SHAP best decisions from fold 5](learner_5_sample_0_best_decisions.png)
### Best decisions for selected sample #2 (Fold #1)
![SHAP best decisions from fold 1](learner_1_sample_1_best_decisions.png)
### Best decisions for selected sample #2 (Fold #2)
![SHAP best decisions from fold 2](learner_2_sample_1_best_decisions.png)
### Best decisions for selected sample #2 (Fold #3)
![SHAP best decisions from fold 3](learner_3_sample_1_best_decisions.png)
### Best decisions for selected sample #2 (Fold #4)
![SHAP best decisions from fold 4](learner_4_sample_1_best_decisions.png)
### Best decisions for selected sample #2 (Fold #5)
![SHAP best decisions from fold 5](learner_5_sample_1_best_decisions.png)
### Best decisions for selected sample #3 (Fold #1)
![SHAP best decisions from fold 1](learner_1_sample_2_best_decisions.png)
### Best decisions for selected sample #3 (Fold #2)
![SHAP best decisions from fold 2](learner_2_sample_2_best_decisions.png)
### Best decisions for selected sample #3 (Fold #3)
![SHAP best decisions from fold 3](learner_3_sample_2_best_decisions.png)
### Best decisions for selected sample #3 (Fold #4)
![SHAP best decisions from fold 4](learner_4_sample_2_best_decisions.png)
### Best decisions for selected sample #3 (Fold #5)
![SHAP best decisions from fold 5](learner_5_sample_2_best_decisions.png)
### Best decisions for selected sample #4 (Fold #1)
![SHAP best decisions from fold 1](learner_1_sample_3_best_decisions.png)
### Best decisions for selected sample #4 (Fold #2)
![SHAP best decisions from fold 2](learner_2_sample_3_best_decisions.png)
### Best decisions for selected sample #4 (Fold #3)
![SHAP best decisions from fold 3](learner_3_sample_3_best_decisions.png)
### Best decisions for selected sample #4 (Fold #4)
![SHAP best decisions from fold 4](learner_4_sample_3_best_decisions.png)
### Best decisions for selected sample #4 (Fold #5)
![SHAP best decisions from fold 5](learner_5_sample_3_best_decisions.png)