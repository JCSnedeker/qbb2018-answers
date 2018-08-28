#!/usr/bin/env python3

import sys

if len(sys.argv)>1:
    f = open( sys.argv[1] )
else:    
    f=sys.stdin

count = 0

for i, line in enumerate( f ):
    if i == 0:
        continue
    fields = line.rstrip("\r\n").split("\t")
    if fields[1].startswith("@"):
        continue
    if len(fields)>12:
        continue
        if fields[12] != "AS:i:0":
            continue
    else:
        count += 1

print(count)