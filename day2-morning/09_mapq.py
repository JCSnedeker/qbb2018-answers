#!/usr/bin/env python3

import sys

if len(sys.argv)>1:
    f = open( sys.argv[1] )
else:    
    f=sys.stdin

count = 0
mapq=0
lengths=0

for i, line in enumerate( f ):
    if i == 0:
        continue
    fields = line.rstrip("\r\n").split("\t")
    if fields[1].startswith("@"):
        continue
    if len(fields)<12:
        continue
    else:
        lengths += 1
        mapq = mapq + int(fields[4])

Final_Value= int(mapq)/int(lengths)
print(Final_Value)
        
    