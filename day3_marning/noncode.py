#!/usr/bin/env python3

#print uniq names from t_data file

import sys

distance = {}
my_dist = 0

for line in open(sys.argv[1]):
    if "#" in line:
        continue
    fields=line.rstrip("\r\n").split("\t")
    types=fields[2]
    chromosome = fields[0]
    stringy = fields[8].split()
    if types != "gene":
        continue
    if chromosome != "3R":
        continue
    if "gene_biotype" in stringy:
        biotype_index = stringy.index("gene_biotype")
        Next_index = biotype_index +1
        if stringy[Next_index] == '"protein_coding";':
            continue
    gene_start=int(fields[3])
    gene_end=int(fields[4])
    find_pos=21378950
    
    if find_pos < gene_start:
        my_dist = gene_start - find_pos
    elif find_pos > gene_end:
        my_dist = find_pos - gene_end
    if "gene_id" in stringy:
        biotype_index = stringy.index("gene_id")
        Next_index = biotype_index +1
        distance[stringy[Next_index]]=my_dist


var=(min(distance, key=distance.get))
print(var, distance[var])