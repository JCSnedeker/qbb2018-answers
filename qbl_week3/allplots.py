#!/usr/bin/env python3

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import fasta

File=open(sys.argv[1])

read_depth = []

for line in File:
    if line.startswith("#"):
        continue
    else:
        lines = line.rstrip("\r\n").split("\t")
        info = lines[7]
        depth = info.split(";")[7].lstrip("DP=")
        depths=depth.strip("\r\n").split(",")
        depths2=depths[0]
        read_depth.append(depths2)

alleles=[]

for line in open(sys.argv[1]):
    if line.startswith("#"):
        continue
    else:
        lines = line.strip("\r\n").split("\t")
        info = lines[7].split(";")
        allele = info[3].split("=")
        values = allele[1].strip("\r\n").split(",")
        val = values[0]
        alleles.append(val)
        
Quality=[]

for line in open(sys.argv[1]):
    if line.startswith("#"):
        continue
    else:
        flines = line.strip("\r\n").split("\t")
        Qual = float(lines[5])
        Quality.append(Qual)
    
Variants = []

for line in open(sys.argv[1]):
    if line.startswith("#"):
        continue
    else:
        lines = line.strip("\r\n").split("\t")
        info = lines[7].split(";")
        #yucky = columns[-1].split("=")
        for item in info:
            last = item.split("=")
            if last[0] == "ANN":
                update= last[1].split("|")
                #print( anewerlist[1] )
                if update[1] == " ":
                    continue
                else:
                    Variants.append(update[1])
        
dicts = {}
for item in Variants:
    if item in dicts:
        dicts[item] += 1
    elif item == "":
        continue
    else:
        dicts[item] = 1
dictkeys = list(dicts.keys())

Final= []
for i in dictkeys:
    if i in dicts:
        Final.append(dicts[i])

fig, axes = plt.subplots(nrows=2,ncols=2)
axes = axes.flatten()

fig.set_size_inches(20,12)

axes[0].hist(alleles, bins = 200, color = "red")
axes[0].set_title('Allele')

axes[1].hist(read_depth, bins = 200, color = "blue")
axes[1].set_title('Depth')

axes[2].hist(Quality, bins = 200, color = "black")
axes[2].set_title('Quality')

axes[3].bar (dictkeys, Final)
axes[3].set_title ("effects of variant")
plt.title( "allele analysis" )

plt.savefig('all_plots.png')
plt.close(fig)