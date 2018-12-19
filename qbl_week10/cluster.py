#!/usr/bin/env python3

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.cluster.hierarchy import linkage, dendrogram
import seaborn as sns; sns.set()

hem_data = pd.read_csv(sys.argv[1], sep="\t", index_col="gene")
#print(hem_data)

links=linkage(hem_data, method='single', metric='euclidean')
print(links)

cmap=sns.diverging_palette(145,280,s=85,l=25,n=7,as_cmap=True)
ax=sns.clustermap(hem_data, cmap=cmap)
ax.savefig("heatmap.png")
plt.close()

#fig, ax = plt.subplots()
#plt.figure(figsize=(15, 8))
#plt.title('Hierarchical Clustering Dendrogram')
#plt.xlabel('sample index')
#plt.ylabel('distance')
#dendrogram(
#    links,
#    leaf_rotation=90.,  # rotates the x axis labels
#    leaf_font_size=8.,  # font size for the x axis labels
#)
#fig.savefig("dendrogram.png")
#plt.close()

#f = open(sys.argv[1], 'r')
#x = f.readlines()
#f.close()

#for i in range(1:len(hem)):
    