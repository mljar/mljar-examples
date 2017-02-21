# MLJAR auto-trading example on Numerai data

This is an example how MLJAR python package can be used to crunch Numer.ai data. This simple script do following:

 1. Login to Numer.ai.
 2. Download dataset.
 3. Upload data into MLJAR and start model search and tuning. It checks for you: Xgboost, LightGBM and Neural Networks and tune each algorithm. At the end the ensemble of all models is created.
 4. Compute predictions on tournament data.
 5. Upload predictions into Numer.ai and print your score :)

With no additional feature transformations I was able to get 0.689 logloss score. What logloss can you get with feature engineering? Good luck!

## How to run it?

 1. Copy the source code of the example.
 2. In `main.py` set NUMERAI_USER, NUMERAI_PASS variables with your Numer.ai credentials.
 3. Set environment variable MLJAR_TOKEN with token from mljar.com (you need to have account there).
 4. To run computation: `python main.py`.

## MLJAR API

The MLJAR platform is used to learn models in this example. The MLJAR makes algorithm search and tuning painless. All computations are in parallel on machines in MLJAR Cloud.

## Numer.ai API

In this example there is Numer.ai API (file numerapi.py) used from [here][1].

[1]: https://github.com/atreichel/NumerAPI
