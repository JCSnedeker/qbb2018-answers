#!/usr/bin/env python3

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

plt.close('all')

position=[]
plist=[]
logp=[]
col=[]
count=0

chrom_order = [
    'chrI','chrII','chrIII','chrIV','chrV',
    'chrVI','chrVII','chrVIII','chrIX',
    'chrXI','chrXII','chrXIII','chrXIV','chrXV',
    'chrXVI','23','26']

colors = ['skyblue', 'sandybrown']
highlights = ['steelblue', 'coral']


for fname in sys.argv[1:]:
    count+=1
    print(count)
    with open(fname) as f:
        header = f.readline() # Reads a single line into the file, and stores it.
        data = {}

        for line in f:
            fields = line.split()
            if fields[-1] == 'NA':
                continue
            # Extract the values we want
            chrom = fields[0]
            pos = int(fields[2])
            p = float(fields[-1])
            logp = -np.log10(p)

            # Store the values
            if chrom not in data:
                data[chrom] = {'positions':[], 'logpvals':[]}
            data[chrom]['positions'].append(pos)
            data[chrom]['logpvals'].append(logp)
            
        fig, ax = plt.subplots(figsize=(20,5))

        offset = 0
        tick_pos = []

        for i,chrom in enumerate(chrom_order):
            # Pull the data for a single chromsome from `data`
            x = np.array(data[chrom]['positions'])
            y = np.array(data[chrom]['logpvals'])

            # Identify which positions are significant
            sig = (y > 5) # An array of booleans, like our `roi` example in Bootcamp

            # Plot the significant values one color, and the insignificant values separately
            plt.scatter(x[sig] + offset, y[sig], c=highlights[i%2], marker='.')
            plt.scatter(x[~sig] + offset, y[~sig], c=colors[i%2], marker='.')

            # Find the offset to use for the tick label and the next chrosome's positions
            maxx = max(x)
            tick_pos.append(offset + maxx/2)
            offset += maxx

        # Label the Chromosomes on the X-axis
        ax.set_xticks(tick_pos)
        ax.set_xticklabels(chrom_order);

        # Add labels and notations to the plot
        ax.axhline(5, c='k', ls=':', label='Significance cutoff')
        ax.legend()
        ax.set_ylabel(r'$\log_{10}(P-value)$')
        ax.set_xlabel('Genomic Position')
        ax.set_title('New_Manhattan_Plot'+ str(count))
        fig.savefig("Manhattan" + str(count) + ".png")
        plt.close();