#!/usr/bin/env python3

#print uniq names from t_data file

import sys

all_genes={}

for line in open(sys.argv[1]):
    if "#" in line:
        continue
    fields=line.rstrip("\r\n").split("\t")
    types=fields[2]
    if types != "gene":
        continue
    stringy = fields[8].split()
    if "gene_biotype" in stringy:
        biotype_index = stringy.index("gene_biotype")
        Next_index = biotype_index +1
        if stringy[Next_index] not in all_genes:
            all_genes[stringy[Next_index]] = 1
        else:
            all_genes[stringy[Next_index]] += 1
print(all_genes)