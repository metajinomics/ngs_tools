#!/usr/bin/python

#python htseq_to_count.py gtf *count
#python htseq_to_count.py inter.gtf /Users/jinchoi/brown_count/*bam.count.txt > count.txt
import sys
gtf = []
prev = ""
for line in open(sys.argv[1],'r'):
    if line[1:] == "#":
        continue
    spl = line.strip().split('\t')
    if (len(spl) > 2 and spl[2] == "exon"):
        ids = spl[8].split('"')[1]
        le = int(spl[4])-int(spl[3])
        gtf.append([ids,str(le)])

count = {}
files = ["gene","length","description"]
for file in sys.argv[2:]:
    files.append(file)
    temp = []
    for line in open(file,'r'):
        if(line[:2] != "__"):
            spl = line.strip().split('\t')
            if(count.has_key(spl[0])):
                temp = count[spl[0]]
                temp.append(spl[1])
                count[spl[0]] = temp
            else:
                temp = [spl[1]]
                count[spl[0]] = temp

print '\t'.join(files)
    
for x in gtf:
    final = [x[0],x[1],x[0]]
    for y in count[x[0]]:
        final.append(y)
    print '\t'.join(final)

