#!/usr/bin/env python3

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv(sys.argv[1])

#soi=df.loc[:,"sex"]=="female"
#df=df.loc[soi,:]
#soi=df.loc[:,"sex"]
#toi=df.loc[:,"stage"]

fpkms={}


for index, sample, sex, stage in df.itertuples():
    filename=os.path.join(sys.argv[2], sample, "t_data.ctab")
    ctab_df = pd.read_table(filename, index_col="t_name")
    fpkm = ctab_df.loc[:,"FPKM"]
    titled = "{0}_{1}".format(sex, stage)
    fpkms[titled]= fpkm
#    fpkm.append(ctab_df.loc[sys.argv[1],"FPKM"])

#fpkm.append(soi)
comp_df=pd.DataFrame(fpkms)
#print(fpkm)
print(comp_df)
#fig, ax = plt.subplots()
#ax.plot(fpkm)
#fig.savefig("timecourse.png")
#plt.close(fig)


