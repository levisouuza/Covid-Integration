
import os
import pandas as pd

archive = r'C:\Users\26497\Downloads\caso_full.csv'

dataset = pd.read_csv(archive)


print(dataset.head(10))
