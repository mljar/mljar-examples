# Summary of Ensemble

## Ensemble structure
| Model                   |   Weight |
|:------------------------|---------:|
| 6_Default_NeuralNetwork |        5 |

### Metric details
|           |   setosa |   versicolor |   virginica |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------:|-------------:|------------:|-----------:|------------:|---------------:|----------:|
| precision |        1 |            1 |           1 |          1 |           1 |              1 | 0.0165346 |
| recall    |        1 |            1 |           1 |          1 |           1 |              1 | 0.0165346 |
| f1-score  |        1 |            1 |           1 |          1 |           1 |              1 | 0.0165346 |
| support   |       11 |           11 |          12 |          1 |          34 |             34 | 0.0165346 |


## Confusion matrix
|                       |   Predicted as setosa |   Predicted as versicolor |   Predicted as virginica |
|:----------------------|----------------------:|--------------------------:|-------------------------:|
| Labeled as setosa     |                    11 |                         0 |                        0 |
| Labeled as versicolor |                     0 |                        11 |                        0 |
| Labeled as virginica  |                     0 |                         0 |                       12 |

## Learning curves
![Learning curves](learning_curves.png)