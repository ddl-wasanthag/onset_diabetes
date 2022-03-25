#!/usr/local/anaconda/bin/python
import sys
import argparse
import json
import pickle

import pandas as pd
import numpy as np

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score, roc_curve, confusion_matrix, accuracy_score, f1_score

def load_data(filename):
    
    dataDF = pd.read_csv(filename)
    dataDF.columns = ["TimesPregnant", "Glucose", "BP", "SkinFold", "Insulin", "BMI", "Pedigree", "Age", "Diabetes"]

    #print(dataDF.head())

    columns_of_interest = ["Glucose", "BP", "SkinFold", "BMI", "Insulin"]
    
    # Impute missing values
    for column in columns_of_interest:
        dataDF[column] = dataDF[column].replace(0, np.NaN)
        mean = int(dataDF[column].mean(skipna=True))
        dataDF[column] = dataDF[column].replace(np.NaN, mean)

    y = dataDF["Diabetes"]
    X = dataDF.drop("Diabetes", 1)

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1234, test_size=0.20)
    
    return X_train, X_test, y_train, y_test

def fit_model(X_train, y_train, lr, depth, ftrs):

    gradient_boost = GradientBoostingClassifier(learning_rate=lr, max_depth=depth, max_features=ftrs, random_state=0)
    gradient_boost.fit(X_train, y_train)

    return gradient_boost

def test_model(model, X_test, y_test):
    
    y_pred = model.predict(X_test)
    
    return f1_score(y_test, y_pred), accuracy_score(y_test, y_pred)

def main(args): 

    parser = argparse.ArgumentParser(description="Train an GB classifier using the UCI Diabetes Data Set. \
                                     This work is licensed \
                                     under the Creative Commons Attribution \
                                     4.0 International License.")
    
    parser.add_argument("--lr",help="Learning rate", 
                        default = 0.05, required=False, type=float)
    parser.add_argument("--depth",help="Maximum depth of the individual regression estimators", 
                        default = 4, required=False, type=int)
    parser.add_argument("--ft",help="Number of features to consider when looking for the best split", 
                        default = 1, required=False, type=int)
    
    args = parser.parse_args()
    
    X_train, X_test, y_train, y_test = load_data("/mnt/data/pima-indians-diabetes.csv")
    
    model = fit_model(X_train, y_train, args.lr, args.depth, args.ft)
    
    f1, acc = test_model(model, X_test, y_test)
    
    print("F1 score: %.2f" % f1)

    print("Accuracy score: %.2f" % acc)
    
    with open('dominostats.json', 'w') as f:
      f.write(json.dumps({"F1 score": f1, "Accuracy": acc}))

    print("Saving model...")
    pickle.dump(model, open("/mnt/model/diabetes_gb.sav", 'wb'))
    print("saved.")
    
if __name__=='__main__':
    main(sys.argv)