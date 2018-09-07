#!/usr/bin/env python3

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import fasta

dna_reader=fasta.FASTAReader(open(sys.argv[1]))
aa_reader=fasta.FASTAReader(open(sys.argv[2]))

my_lst_str={}
nuc_lists = []
for (dna_id, dna), (aa_id, aa) in zip(dna_reader, aa_reader):
    nuc_list=[]
    for i in range(len(aa)):
        a=aa[i]
        nuc=dna[i*3:(i+1)*3]
        if a=="-":
            nuc="---"
        nuc_list.append(nuc)
    sequence= ''.join(map(str, nuc_list))
    my_lst_str[dna_id] = sequence
    nuc_lists.append(nuc_list)

#print(my_lst_str)
print(nuc_lists)
        
            