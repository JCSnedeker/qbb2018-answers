#!/usr/bin/env python3

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import fasta

count = 0
count2 = 0
plt.figure()
for gene in open( sys.argv[1] ):
    count += 1
    if count == 1:
        continue
    else:
        gene = gene.rstrip('\r\n').split('\t')
        start, end= int(gene[1]), int(gene[2])
        plt.plot( [start, end], [count2, count2 + abs(start - end)] )
        count2 += abs(start-end)

plt.xlim( 0, 100000 )
plt.ylim( 0, 100000 )
plt.xlabel( 'reference' )
plt.ylabel( 'query' )
plt.title( "velvet low read" )
plt.savefig( "velvet_low_read.png")
plt.close()