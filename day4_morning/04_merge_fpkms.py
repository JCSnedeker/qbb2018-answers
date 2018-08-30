#!/usr/bin/env python3

"""
Prints files where sum of FPKM is greater than threshold
"""

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

d={}
Total=0
f=float(sys.argv[1])

for name in range(2,len(sys.argv)):
    name1=sys.argv[name].split(os.sep)[-2]
    fpkm1=pd.read_csv(sys.argv[name], sep="\t", index_col="t_name").loc[:,"FPKM"]
    d[name1]=fpkm1
    d_df=pd.DataFrame(d)
    Total+=fpkm1


roi=Total > f
d_df.loc[roi,:].to_csv(sys.stdout, sep="\t")



