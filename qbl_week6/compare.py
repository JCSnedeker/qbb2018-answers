#!/usr/bin/env python3

import sys
import csv
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

Gain=open(sys.argv[1])
#overlap.bed
Lost=open(sys.argv[2])
#nonoverlap.bed
feat=open(sys.argv[3])
#Mus.bed

options={}

for line in feat:
    fields=line.rstrip("\r\n").split("\t")
    start=int(fields[1])
    end=int(fields[2])
    feature=fields[3]
    for a in range(start,end):
        options[a]=feature
        
num_gain=0
all_gain=[]
for i, line in enumerate(Gain):
    num_gain+=1
    fg=[]
    fields=line.rstrip("\r\n").split("\t")
    start=int(fields[1])
    end=int(fields[2])
    for a in range(start, end):
        if a in options:
            feat_g=options[a]
            if feat_g not in fg:
                fg.append(feat_g)
    all_gain.append(fg)
    fg=[]

gain_in=0
gain_ex=0
gain_pro=0

for i in all_gain:
    if len(i) == 0:
        continue
    for a in i:
        if a =="intron":
            gain_in +=1
        elif a=="exon":
            gain_ex +=1
        elif a =="promoter":
            gain_pro+=1
        else:
            continue
            
print("The number of gained CTCF sites in introns is: " + str(gain_in))
print("The number of gained CTCF sites in exons is: " + str(gain_ex))
print("The number of gained CTCF sites in promoters is: " + str(gain_pro))

num_loss=0
all_loss=[]
for i, line in enumerate(Lost):
    num_loss+=1
    fg=[]
    fields=line.rstrip("\r\n").split("\t")
    start=int(fields[1])
    end=int(fields[2])
    for a in range(start, end):
        if a in options:
            feat_l=options[a]
            if feat_l not in fg:
                fg.append(feat_l)
    all_loss.append(fg)
    fg=[]

loss_in=0
loss_ex=0
loss_pro=0

for i in all_loss:
    if len(i) == 0:
        continue
    for a in i:
        if a =="intron":
            loss_in +=1
        elif a=="exon":
            loss_ex +=1
        elif a =="promoter":
            loss_pro+=1
        else:
            continue
        
print("The number of lost CTCF sites in introns is: " + str(loss_in))
print("The number of lost CTCF sites in exons is: " + str(loss_ex))
print("The number of lost CTCF sites in promoters is: " + str(loss_pro))

fig, (ax1, ax2)=plt.subplots(ncols=2, figsize=(15,10))
ax1.bar("total gained", num_gain, color="r")
ax1.bar("total lost", num_loss, color="b")
ax1.set_ylabel("Number of CTCF sites")
ax1.set_title("Total change in CTCF occupancy")

ax2.bar("exons gained", gain_ex, color="r")
ax2.bar("exons lost", loss_ex, color="b")
ax2.bar("intron gained", gain_in, color="r")
ax2.bar("intron lost", loss_in, color="b")
ax2.bar("pro. gained", gain_pro, color="r")
ax2.bar("pro. lost", loss_pro, color="b")
ax2.set_ylabel("Number of CTCF sites")
ax2.set_title("Regional change in CTCF occupancy")

fig.savefig("CTCF_chip_seq.png")
plt.close(fig)

