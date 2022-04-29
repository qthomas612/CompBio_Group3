# Tutorial for local blast: https://www.tutorialspoint.com/biopython/biopython_overview_of_blast.htm

from Bio.Blast.Applications import NcbiblastnCommandline 
from Bio.Blast import NCBIXML
from Bio import SeqIO 
import os, numpy









# create a blast database of SPAdes contigs
os.system("makeblastdb -in /output/Results/SPAdes/contigs.fasta -parse_seqids -dbtype nucl -out /output/Results/blast_db/SPAdes")

blastn_cline = NcbiblastnCommandline(query = "/output/Results/plasmidSPAdes/contigs.fasta", db = "/output/Results/blast_db/SPAdes", outfmt = 5, out = "/output/plasmidSPAdes/plasmidSPAdes_blast.xml") 

stdout, stderr = blastn_cline()

results = [["plasmidSPAdes plasmid","closest SPAdes contig"]]

for record in NCBIXML.parse(open("/output/plasmidSPAdes/plasmidSPAdes_blast.xml")): 
    if record.alignments:
        query = record.query.split("_component_")[0]
        match = record.alignments[0].title.split(" No definition line")[0]
        results.append([query,match])
        #results[record.query] = record.alignments[0].title
results
numpy.savetxt("/output/plasmidSPAdes_closest_conitg.csv", results, delimiter =", ", fmt ='% s')
