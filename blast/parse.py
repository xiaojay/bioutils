#coding=utf-8

#parse blast xml result file

import sys
from Bio.Blast import NCBIXML
n = 10

fn = sys.argv[1]
blast_records = NCBIXML.parse(open(fn))

for r in blast_records:
    for a in r.alignments[:n]:
        h = a.hsps[0]
        line = [r.query, r.query_length,a.title, a.length, h.expect, h.score, h.align_length]
        line = [str(i) for i in line]
        print '\t'.join(line)
