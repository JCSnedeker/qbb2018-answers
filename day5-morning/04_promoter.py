#!/usr/bin/env python3

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

df=pd.read_csv(sys.argv[1], sep="\t")
#Starter=df.loc[:,"start"]
Starter = df['start'].tolist()

Before=[]
After=[]

for i in range(len(Starter)):
    Before.append(Starter[i])
    Before[i]=Before[i]-500
    After.append(Starter[i])
    After[i]=After[i]+500
    if Before[i]<0:
        Before[i]=1

se1 = pd.Series(Before)
df['before'] = se1.values

se2 = pd.Series(After)
df['after'] = se2.values

df1=df[['chr','before','after','t_name']]

final=pd.DataFrame.to_csv(df1, sep="\t", header=False, index=False)

print(final)

