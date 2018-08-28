#!/bin/bash

cd ~/qbb2018-answers/day1-afternoon/SRR072893
samtools idxstats SRR072893.sorted.bam | cut -f 1,3 | head -7



