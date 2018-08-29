#!/usr/bin/env python3

#print uniq names from t_data file

import sys
import fasta

target=fasta.FASTAReader(open(sys.argv[1]))
query=fasta.FASTAReader(open(sys.argv[2]))
k1=sys.argv[3]
k=int(k1)

kmers={}


for ident, sequence in query:
    for i in range(0, len(sequence)-k):
        kmer=sequence[i:i+k]
        if kmer not in kmers:
            kmers[kmer]=[i]
        else:
            kmers[kmer].append(i)

for ident, sequence in target:
    for i in range(0, len(sequence)-k):
        kmer=sequence[i:i+k]
        if kmer in kmers:
            print(ident, i, kmers[kmer], kmer)
        
            
