#!/usr/bin/env python3

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import fasta
# from Bio.codonalign.codonseq import _get_codon_list, CodonSeq, cal_dn_ds

dna_reader=fasta.FASTAReader(open(sys.argv[1]))
aa_reader=fasta.FASTAReader(open(sys.argv[2]))
query_reader=fasta.FASTAReader(open(sys.argv[3]))

seq_list=[]
my_lst_str={}
nuc_lists = []
for (dna_id, dna), (aa_id, aa) in zip(dna_reader, aa_reader):
    j = 0
    nuc_list=[]
    for i in range(len(aa)):
        a=aa[i]
        nuc=dna[j:j + 3]
        if a=="-":
            nuc="---"
            nuc_list.append(nuc)
        else:
            nuc_list.append(nuc)
            j += 3
    sequence= ''.join(map(str, nuc_list))
    seq_list.append(sequence)
    my_lst_str[dna_id] = sequence
    nuc_lists.append(nuc_list)

#print(nuc_lists)


codons=[]
i=0
for (qu_id, seq) in query_reader:
    query_seq=seq
    for char in seq:
        codons.append(seq[i:i+3])
        i=i+3
        if i > len(seq):
            break

table = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                 
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
}
# dN_dS=[]
# for i in range(len(seq_list)):
#     var=cal_dn_ds(query_seq, seq_list[i], method='NG86', codon_table=table, k=1, cfreq=None)
#     dN_dS.append(var)
    
#print(dN_dS)

# for homologous seq
# for each codon

#query_prot=table[nuc_lists[0][100]]
#print(query_prot)

ds_list=[]
dn_list=[]
for i in range(len(nuc_lists[0])):
    dS=0
    dN=0
    #print(i)
    for j in range(1,len(nuc_lists)):
        #print(nuc_lists[i][j], nuc_lists[0][j])
        if nuc_lists[j][i]==nuc_lists[0][i]:
            pass
   #      elif nuc_lists[0][j]=="---":
   #          pass
   #      elif nuc_lists[i][j]=="---":
   #          pass
        elif nuc_lists[j][i] not in table:
            pass
        elif nuc_lists[0][i] not in table:
            pass
        elif len(nuc_lists[j][i]) != 3:
            pass
        elif len(nuc_lists[0][i]) != 3:
            pass
        elif table[nuc_lists[0][i]] == table[nuc_lists[j][i]]:
            dS+=1
        else:
            dN+=1
    ds_list.append(dS)
    dn_list.append(dN)
#
# print(ds_list)
# print(dn_list)

# def twoSampZ(X1, X2, mudiff, sd1, sd2, n1, n2):
#     from numpy import sqrt, abs, round
#     from scipy.stats import norm
#     pooledSE = sqrt(sd1**2/n1 + sd2**2/n2)
#     z = ((X1 - X2) - mudiff)/pooledSE
#     pval = 2*(1 - norm.cdf(abs(z)))
#     return round(z, 3), round(pval, 4)
#
#
# x1=np.mean(ds_list)
# x2=np.mean(dn_list)
# s1=np.std(ds_list)
# s2=np.std(dn_list)
# n1=len(ds_list)
# n2=len(dn_list)
# z, p = twoSampZ(x1, x2, 0, s1, s2, n1, n2)
# print(x1)
# print(x2)

dist=[]
for i in range(0,6614):
    mean_diff=ds_list[i]-dn_list[i]
    dist.append(mean_diff)

StE=np.std(dist)/np.sqrt(len(dist))

zi=[]
for i in range(0,6614):
    z=dist[i]/StE
    zi.append(z)
print(zi)

x_vals=range(1,6615)

y_vals=[]
for i in range(0,6614):
    y=4.327
    y_vals.append(y)

y_vals2=[]
for i in range(0,6614):
    y=-4.327
    y_vals2.append(y)
    

fig, ax =plt.subplots()
plt.scatter(x_vals, zi, s=.1)
plt.plot(x_vals, y_vals, '--', color='red')
plt.plot(x_vals, y_vals2, '--', color='red')
plt.ylabel('z values')
plt.xlabel('codon position')
plt.title('Positional Z values Across Genome')
fig.savefig("compare.png")
plt.close(fig)
# def translate(seq):
#
#     table = {
#         'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
#         'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
#         'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
#         'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
#         'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
#         'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
#         'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
#         'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
#         'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
#         'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
#         'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
#         'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
#         'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
#         'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
#         'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
#         'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
#     }
#     protein =""
#     if len(seq)%3 == 0:
#         for i in range(0, len(seq), 3):
#             codon = seq[i:i + 3]
#             protein+= table[codon]
#     return protein
#
# query_prot=translate(query_seq)
# #print(query_prot)
#
# syn=0
# nonsyn=0
# for lists in nuc_lists:
#     for i in range(len(codons)):
#         if lists[i] == "---":
#             continue
#         if lists[i] == codons[i]:
#             continue
#
#
#
# #print(codons)
#
# # new_list=[]
# # for (dna_id, dna), (aa_id, aa) in zip(query_reader, aa_reader):
# #     for i in range(len(aa)):
# #         a=aa[i]
# #         nuc=dna[i*3:(i+1)*3]
# #         new_list.append(nuc)
# #
# # print(new_list)
#
#
# #
#
#
#