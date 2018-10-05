#!/usr/bin/env python3

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pca=open(sys.argv[1])
vcf_file=open(sys.argv[2])

pca1=[]
pca2=[]
allele_freq=[]

for line in pca:
    lines = line.rstrip("\r\n").split(" ")
    pca1.append(float(lines[2]))
    pca2.append(float(lines[3]))
    
for line in vcf_file:
    if line.startswith("#"):
        continue
    fields=line.split()
    info=fields[7]
    for id_val in info.split(";"):
        id, val = id_val.split("=")
        if id=="AF":
            allele_freq.append(float(val.split(',')[0]))

fig, ax = plt.subplots()
ax.scatter(pca1,pca2)
fig.suptitle('PCA', fontsize=20)
plt.xlabel('PCA1')
plt.ylabel('PCA2')
fig.savefig("pca.png")
plt.close(fig)

fig, ax = plt.subplots()
ax.hist(allele_freq, bins=100)
fig.suptitle('Allele Frequency', fontsize=20)
plt.xlabel('AF')
plt.ylabel('Frequency')
fig.savefig("AF.png")
plt.close(fig)
