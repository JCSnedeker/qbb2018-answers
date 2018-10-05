#!/usr/bin/env python3

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

position=[]
plist=[]
logp=[]
col=[]
count=0


for fname in sys.argv[1:]:
    count+=1
    print(count)
    with open(fname) as f:
        for line in f:
            if "NA" in line or "BETA" in line:
                continue
            else:
                lines=line.rstrip("\r\n").split()
                pos=float(lines[2])
                position.append(pos)
                p=float(lines[8])
                plist.append(p)
                logs=-(math.log(p, 10))
                logp.append(logs)
                if logs<5:
                    col.append("blue")
                else:
                    col.append("red")
#                threshold=int(logs)
#                posit=int(pos)
#                col = np.where(posit<1,'k',np.where(threshold>5,'b','r'))
        fig, ax = plt.subplots()
        plt.scatter(position, logp, color = col, alpha = 0.7)
        ax.set_xlabel("Position")
        ax.set_ylabel("-log(p-value)")
        fig.savefig("Manhattan" + str(count) + ".png")
        plt.close()
    pass