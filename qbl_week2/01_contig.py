#!/usr/bin/env python3

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import fasta

files=fasta.FASTAReader(open(sys.argv[1]))

contig_list=[]
len_list=[]

for header, contig in files:
    contig_list.append(contig)

for i in range(len(contig_list)):
    length=len(contig_list[i])
    len_list.append(length)

len_list.sort()

n_len=sum(len_list)//2

tots=0
    
print("Num Contig: ", len(contig_list))
print("Min Value: ", len_list[0])
print("Max Value: ", len_list[-1])
print("Med Value: ", len_list[len(len_list)//2])
print("Avg Value: ", sum(len_list)//len(len_list))

for i in range(len(len_list)):
    tots+=len_list[i]
    if tots > n_len:
        print("N50 Value: ", len_list[i])
        break
