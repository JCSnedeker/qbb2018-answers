#!/usr/bin/env python3

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.cluster.hierarchy import linkage, dendrogram
import seaborn as sns; sns.set()
from copy import deepcopy
from sklearn.cluster import KMeans

hem_data = pd.read_csv(sys.argv[1], sep="\t", index_col="gene").loc[:, ("CFU", "poly")]
df=hem_data.values
Names=hem_data.columns.values.tolist()
#print(df)

array=linkage(df, 'ward')

kmeans=KMeans(n_clusters=4)
kmeans.fit(array)

#print(kmeans.cluster_centers_)
y_km=kmeans.predict(array)

fig, ax = plt.subplots()
plt.scatter(array[:,0], array[:,1], c=y_km, s=30, cmap="viridis")
centers=kmeans.cluster_centers_
plt.scatter(centers[:,0], centers[:,1], c="black", s=100)
fig.savefig("kmeans_plot.png")
plt.close(fig)