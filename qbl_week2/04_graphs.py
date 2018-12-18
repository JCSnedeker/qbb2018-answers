#!/usr/bin/env python3

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import fasta

plt.style.use('ggplot')

files = open(sys.argv[1])
filename = (sys.argv[1].split("_"))[1]

fig, ax = plt.subplots(figsize=(25, 10))

x_pos = 0
for line in files:
    if line.startswith("name1"):
        continue
    if line.startswith("#"):
        continue
    else:
        fields = line.rstrip("\r\n").split("\t")
        start = int(fields[4])
        end = int(fields[5])
        length = end-start
    x = np.linspace(x_pos,x_pos+length)  
    y = np.linspace(start,end)
    ax.plot(x, y)
    x_pos += length
    

ax.set_xlabel("Contigs")
ax.set_ylabel("Reference position")
ax.set_title(filename)
fig.savefig(filename + "H.png")
plt.close(fig)