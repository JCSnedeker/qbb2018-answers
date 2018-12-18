#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt

files=open(sys.argv[1])
di = {}

for line in files:
    fields = line.rstrip("\t").split()
    a = float(fields[2])
    if a not in di:
        di[a] = 1
    else:
        di[a] += 1
        
fig, ax = plt.subplots()
for key in di:
    plt.scatter([key], di[key])
ax.set_xlabel("Size")
ax.set_ylabel("Motif Count")
ax.set_title("Sequence Position")
fig.savefig("meme.png")
plt.close()