#!/usr/bin/env python3

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import statsmodels.formula.api as sm

df=pd.read_csv(sys.argv[6], sep="\t")
Express = df.loc[:,'FPKM']


df1=pd.read_csv(sys.argv[1], sep="\t")
df1_1=df1.iloc[:,-1]
df2=pd.read_csv(sys.argv[2], sep="\t")
df2_1=df1.iloc[:,-1]
df3=pd.read_csv(sys.argv[3], sep="\t")
df3_1=df1.iloc[:,-1]
df4=pd.read_csv(sys.argv[4], sep="\t")
df4_1=df1.iloc[:,-1]
df5=pd.read_csv(sys.argv[5], sep="\t")
df5_1=df1.iloc[:,-1]

His_mod = pd.concat([df1_1, df2_1, df3_1, df4_1, df5_1, Express], axis=1)
His_mod.columns=["H3K4me3", "H3K4me1", "H3K27me3", "H3K27ac", "H3K9ac", "FPKM"]


Regress=sm.ols(formula='FPKM ~ H3K4me3 + H3K4me1 + H3K27me3 + H3K27ac + H3K9ac', data=His_mod)
results=Regress.fit()
print(results.summary())

fig, ax =plt.subplots()
ax.set_title("Plot of residuals")
plt.hist(results.resid_pearson)
plt.ylabel('Count')
plt.xlabel('Normalized residuals')
fig.savefig("Residuals.png")
plt.close()