#!/usr/bin/env python3

#print uniq names from t_data file

import sys

count=0

for line in open(sys.argv[1]):
    if "#" in line:
        continue
    fields=line.rstrip("\r\n").split("\t")
    
    types=fields[2]
    if types != "gene":
        continue
    stringy = fields[8].split()
    
    if "gene_biotype" and '"protein_coding";' in stringy:
        count += 1
        
print(count)