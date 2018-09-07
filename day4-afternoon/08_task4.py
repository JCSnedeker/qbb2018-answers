#!/usr/bin/env python3

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv( sys.argv[1], sep="\t", index_col="t_name" )
name1 = sys.argv[1].split( os.sep)[-2]
fpkm1 = pd.read_csv( sys.argv[1], sep="\t", index_col= "t_name").loc[:,"FPKM"]
name2 = sys.argv[2].split( os.sep)[-2]
fpkm2 = pd.read_csv( sys.argv[2], sep="\t", index_col= "t_name").loc[:,"FPKM"]

m = (fpkm1/fpkm2)
log_m = np.log( m + 1)
a = (1/2) * (fpkm1 + fpkm2)
log_a = np.log( a +1)

fig, ax = plt.subplots()
fig.suptitle( "MA plot" )
ax.set_xlabel("log(fpkm) " + str(name1))
ax.scatter(log_a,log_m, alpha= 0.2)
ax.set_ylabel("log(fpkm) " + str(name2))
fig.savefig("day4MA.png")
plt.close(fig)