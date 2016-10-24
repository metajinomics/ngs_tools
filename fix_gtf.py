#python fix_gtf.py gff > gtf

import sys
for line in open(sys.argv[1],'r'):
    if(line[:1] == "#"):
        continue
    spl = line.strip().split('\t')
    ids = spl[0].split('_')
    des = spl[8].split(';')
    geneid = des[0].split('=')
    firstid = 'gene_id \"' + geneid[1] +'\";'
    temp = ';'.join(des[1:])
    finaldes = firstid + temp
    result = [spl[0],spl[1],"exon"]
    for i in range(3,len(spl)-1):
        result.append(spl[i])
    result.append(finaldes)
    print '\t'.join(result)

