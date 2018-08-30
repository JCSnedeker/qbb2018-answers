#!/usr/bin/env python3

"""
Prints files where sum of FPKM is greater than threshold
"""

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

name1=sys.argv[1].split(os.sep)[-2]
fpkm1=pd.read_csv(sys.argv[1], sep="\t", index_col="t_name").loc[:,"FPKM"]

name2=sys.argv[2].split(os.sep)[-2]
fpkm2=pd.read_csv(sys.argv[2], sep="\t", index_col="t_name").loc[:,"FPKM"]

var=linregress(fpkm1, fpkm2)
print(var)

m=1.4665202478798527
b=0

fig, ax =plt.subplots()
ax.scatter(fpkm1, fpkm2, s=3, color="red", alpha=0.15)
ax.set_yscale('log')
ax.set_xscale('log')
ax.set_xlabel("FPKM1")
ax.set_ylabel("FPKM2")
plt.axis([.001, 10000,.001, 10000])
axes = plt.gca()
x_vals = np.array(axes.get_xlim())
y_vals = b + m * x_vals
plt.plot(x_vals, y_vals, '--')
fig.suptitle("FPKM compare")
fig.savefig("compare.png")
plt.close(fig)