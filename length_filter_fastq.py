#this script filter short sequence
#usage: python length_filter_fastq.py fastqfile length > outputfile
#python length_filter_fasta.py fasta.fq 300 > fasta_over300.fq

import sys
def check_length(seqs,cu):
    if(len(seqs[1]) >= cu):
        for x in seqs:
            print x

def main():
    fread = open(sys.argv[1],'r')
    cu = int(sys.argv[2])
    seqs = []
    for n,line in enumerate(fread):
        if( n%4 == 3):
            seqs.append(line.strip())
            check_length(seqs,cu)
        else:
            seqs.append(line.strip())

if __name__ == '__main__':
    main()
