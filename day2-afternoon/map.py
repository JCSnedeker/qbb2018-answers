#!/usr/bin/env python3

#print uniq names from t_data file

import sys

map1=[]
map2={}

for i, line in enumerate(open(sys.argv[2])):
    if i==0:
        continue
    if "DROME" in line and "FBgn" in line:
        clean=line.rstrip("\r\n").split()
        uniprot=clean[3]
        Flybase=clean[2]
        map2.update({uniprot : Flybase})
        
        
for key in map2:
    print(key + "    " + map2[key])
    
