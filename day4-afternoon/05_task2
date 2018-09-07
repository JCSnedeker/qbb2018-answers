#!/usr/bin/env python3

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def timecourse( csv, gender, gene ):
    df = pd.read_csv( csv )
    soi = df.loc[:,"sex"] == gender 
    frames = df.loc[soi,:]
    fpkms_avg = []
    
    
    for index, sample, sex, stage in frames.itertuples():
        filename = os.path.join( sys.argv[2], sample, "t_data.ctab")
        ctab_df = pd.read_table( filename, index_col="t_name")
        roi = ctab_df.loc[:,"gene_name"] == gene
        fpkms = ctab_df.loc[roi,"FPKM"]
        fpkms_avg.append(np.mean(fpkms))
    return fpkms_avg
    
for item in sys.argv[3:]:  
    var = timecourse(sys.argv[1], "female", item)
    stages = ["10", "11", "12", "13", "14A", "14B", "14C", "14D"]


    fig, ax = plt.subplots()
    ax.plot(var,  color= "blue", label= "fpkms_avg" )
    plt.suptitle= ( item + "mean txpt fpkms" )
    plt.tight_layout()
    ax.set_ylabel("FPKMs")
    ax.set_xlabel("stage")
    plt.tight_layout()
    box=ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height] )
    ax.legend(loc='center left', bbox_to_anchor=(1,0.5), frameon = False)
    fig.savefig("{0}.png".format(item))
    plt.close( fig )
