# Tutorial for local blast: https://www.tutorialspoint.com/biopython/biopython_overview_of_blast.htm

from Bio.Blast.Applications import NcbiblastnCommandline 
from Bio.Blast import NCBIXML
from Bio import SeqIO 
import os


# create a blast database of SPAdes contigs
os.system("makeblastdb -in /output/Results/SPAdes/contigs.fasta -parse_seqids -dbtype nucl -out /output/Results/blast_db/SPADes")

blastn_cline = NcbiblastnCommandline(query = "/output/Results/plasmidSPAdes/contigs.fasta", db = "/output/Results/blast_db/SPADes", outfmt = 5, out = "/output/plasmidSPAdes/plasmidSPAdes_blast.xml") 

stdout, stderr = blastn_cline()

results = dict()

for record in NCBIXML.parse(open("results.xml")): 
    if record.alignments:
        record.alignments.hsps.expect


        results[record.query]

        print("\n") 
        print("query: %s" % record.query[:100]) 
        for align in record.alignments:
            minE = min()
            for hsp in align.hsps:
                if hsp.expect < E_VALUE_THRESH: 
                    print("match: %s " % align.title[:100])