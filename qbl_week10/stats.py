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
from scipy.stats import ttest_ind

hem_data = pd.read_table(sys.argv[1], sep="\t", header=0, index_col="gene").loc[:, ("CFU", "mys", "poly", "unk")].dropna()
v1=["CFU", "mys"]
v2=["poly", "unk"]
t,p=ttest_ind(hem_data[v1], hem_data[v2], axis=1)
hem_data["p_val"]=p
hem_data=hem_data.mask(hem_data["p_val"]>.05).dropna(how="any").sort_values("p_val")
print(hem_data.ix[:,4].to_csv(sep="\t"))