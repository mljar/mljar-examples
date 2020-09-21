# Summary of 6_Default_NeuralNetwork_SelectedFeatures

## Neural Network
- **dense_layers**: 2
- **dense_1_size**: 32
- **dense_2_size**: 16
- **dropout**: 0
- **learning_rate**: 0.05
- **momentum**: 0.9
- **decay**: 0.001
- **explain_level**: 2

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.75
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

4.3 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.695517 |  nan        |
| auc       | 0.523672 |  nan        |
| f1        | 0.680739 |    0.372357 |
| accuracy  | 0.568    |    0.488371 |
| precision | 0.566038 |    0.488371 |
| recall    | 1        |    0.372357 |
| mcc       | 0.132351 |    0.488371 |


## Confusion matrix (at threshold=0.488371)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                       0 |                     121 |
| Labeled as positive |                       0 |                     129 |

## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)