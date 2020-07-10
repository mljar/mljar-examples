# AutoML Leaderboard

| Best model   | name                    | model_type     | metric_type   |   metric_value |   train_time | Link                                              |
|:-------------|:------------------------|:---------------|:--------------|---------------:|-------------:|:--------------------------------------------------|
|              | 1_Baseline              | Baseline       | rmse          |        9.65827 |         0.03 | [Results link](1_Baseline/README.md)              |
|              | 2_DecisionTree          | Decision Tree  | rmse          |        5.36558 |         7.33 | [Results link](2_DecisionTree/README.md)          |
|              | 3_Linear                | Linear         | rmse          |        4.64713 |         2.48 | [Results link](3_Linear/README.md)                |
|              | 4_Default_RandomForest  | Random Forest  | rmse          |        4.25229 |         3.88 | [Results link](4_Default_RandomForest/README.md)  |
|              | 5_Default_Xgboost       | Xgboost        | rmse          |        3.20896 |         8.07 | [Results link](5_Default_Xgboost/README.md)       |
|              | 6_Default_NeuralNetwork | Neural Network | rmse          |        3.02272 |         2.99 | [Results link](6_Default_NeuralNetwork/README.md) |
| **the best** | Ensemble                | Ensemble       | rmse          |        2.83816 |         0.09 | [Results link](Ensemble/README.md)                |

### AutoML Performance
![AutoML Performance](ldb_performance.png)

### AutoML Performance Boxplot
![AutoML Performance Boxplot](ldb_performance_boxplot.png)