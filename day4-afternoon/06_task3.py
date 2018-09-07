#!/usr/bin/env python3

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def timecourse( csv, gender ):
    df = pd.read_csv( csv )
    soi = df.loc[:,"sex"] == gender 
    frames = df.loc[soi,:]
    fpkms = []
    
    for index, sample, sex, stage in frames.itertuples():
        filename = os.path.join( sys.argv[4], sample, "t_data.ctab")
        ctab_df = pd.read_table( filename, index_col="t_name")
        fpkms.append( ctab_df.loc[sys.argv[1],"FPKM"] )
    return fpkms

females_fpkms = timecourse( sys.argv[2], "female") 
males_fpkms = timecourse( sys.argv[2], "male")

females_fpkmsREP =timecourse( sys.argv[3], "female") 
males_fpkmsREP = timecourse( sys.argv[3], "male")

stages = ["10", "11", "12", "13", "14A", "14B", "14C", "14D"]

fig, ax = plt.subplots()
ax.plot( stages, males_fpkms, color= "blue", label= "male" )
ax.plot( stages, females_fpkms, color= "red", label= "female" )
ax.plot( stages, males_fpkmsREP, color= "orange", label= "male Replicates")
ax.plot( stages, females_fpkmsREP, color= "green", label= "female Replicates")
ax.set_title=( sys.argv[1] )
plt.tight_layout()
ax.set_ylabel("FPKMs")
ax.set_xlabel("stage")
plt.tight_layout()
box=ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height] )
ax.legend(loc='center left', bbox_to_anchor=(1,0.5), frameon = False)
plt.xticks(stages, rotation= "vertical")
fig.savefig( "timecourseMF.png")
plt.close( fig )
