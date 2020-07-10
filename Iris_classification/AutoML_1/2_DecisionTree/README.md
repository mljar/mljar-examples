# Summary of 2_DecisionTree

## Decision Tree
- **criterion**: gini
- **max_depth**: 3
- **num_class**: 3
- **explain_level**: 2

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.75
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

3.7 seconds

### Metric details
|           |   setosa |   versicolor |   virginica |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------:|-------------:|------------:|-----------:|------------:|---------------:|----------:|
| precision |        1 |     0.916667 |    1        |   0.970588 |    0.972222 |       0.973039 |  0.112207 |
| recall    |        1 |     1        |    0.916667 |   0.970588 |    0.972222 |       0.970588 |  0.112207 |
| f1-score  |        1 |     0.956522 |    0.956522 |   0.970588 |    0.971014 |       0.970588 |  0.112207 |
| support   |       11 |    11        |   12        |   0.970588 |   34        |      34        |  0.112207 |


## Confusion matrix
|                       |   Predicted as setosa |   Predicted as versicolor |   Predicted as virginica |
|:----------------------|----------------------:|--------------------------:|-------------------------:|
| Labeled as setosa     |                    11 |                         0 |                        0 |
| Labeled as versicolor |                     0 |                        11 |                        0 |
| Labeled as virginica  |                     0 |                         1 |                       11 |

## Learning curves
![Learning curves](learning_curves.png)

## Tree visualizations

### Tree #1
![Tree 1](learner_1_tree.svg)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)