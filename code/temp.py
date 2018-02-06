# -*- coding: utf-8 -*-
"""
Created on Wed Jan 03 15:02:54 2018

@author: chenxi11
"""
from __future__ import print_function
import csv
import os
import sys
import pandas as pd

#os.chdir('F:\\Kaggle\\MercariPriceSuggestionChallenge\\data')

def load_tsv(path, hasColname, sep = '\t'):
        
    with open(path, encoding='utf-8') as tsvfile:
        reader = csv.reader(tsvfile, delimiter=sep)
        mydataList = []
        for row in reader:
            mydataList.append(row)            
    
    if hasColname:
        return pd.DataFrame(mydataList[1:], columns = mydataList[0])
    else:
        return pd.DataFrame(mydataList)

mypath = 'F:\\Kaggle\\MercariPriceSuggestionChallenge\\data\\'
#a = pd.DataFrame.from_csv(mypath + 'train.tsv', sep='\t')
train = load_tsv(mypath + 'train.tsv', True)
test = load_tsv(mypath + 'test.tsv', True)
temp = train[:1000]

temp.dtypes
temp.describe()

train.describe()