#python fix_gtf.py gff > gtf

import sys
for line in open(sys.argv[1],'r'):
    if(line[:1] == "#"):
        continue
    spl = line.strip().split('\t')
    ids = spl[0].split('_')
    fid = '_'.join(ids[:-3])
    result = [fid,spl[1],"exon"]
    for i in range(3,len(spl)):
        result.append(spl[i])
    print '\t'.join(result)

