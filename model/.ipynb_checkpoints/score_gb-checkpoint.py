#!/usr/local/anaconda/bin/python

import pickle
import sys

import numpy as np

def score(timesPregnant, glucose, bp, skinFold, insulin, BMI, pedigree, age):
    model = pickle.load(open("model/diabetes_gb.sav", 'rb'))
    result = model.predict_proba([[timesPregnant, glucose, bp, skinFold, insulin, BMI, pedigree, age]]) 
    return result
    
def main(args):
    
    #print(score(3,137,110,35,1,40,3,30))
    print(score(3,137,110,35,1,40,3,30))
    
if __name__=='__main__':
    main(sys.argv)
    