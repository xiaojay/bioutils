#coding=utf-8
from Bio import SeqIO
import sys

fn = sys.argv[1]
cds = []
for gb in SeqIO.parse(fn, 'genbank'):
    i = 0
    for f in gb.features:
        if f.type == 'CDS':
            cds.append(f.extract(gb))
            i += 1
    print gb.name, i

output_fn = fn + '.cds.fasta'
SeqIO.write(cds, output_fn, "fasta")

