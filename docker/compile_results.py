# Tutorial for local blast: https://www.tutorialspoint.com/biopython/biopython_overview_of_blast.htm

from Bio.Blast.Applications import NcbiblastnCommandline 
from Bio.Blast import NCBIXML
from Bio import SeqIO 
import os, numpy


#### SPAdes
contigs = []

with open("/output/SPAdes/contigs.fasta") as handle:
    record = list(SeqIO.parse(handle, "fasta"))
    for seq in record:
        contigs.append(seq.id)

# for testing
with open("/home/tkosciuch/Results01180/SPAdes/contigs.fasta") as handle:
    record = list(SeqIO.parse(handle, "fasta"))
    for seq in record:
        contigs.append(seq.id)

#### platon
platon_plasmid = []
platon_chromosome = []

with open("/home/tkosciuch/Results01180/platon/contigs.plasmid.fasta") as handle:
    record = list(SeqIO.parse(handle, "fasta"))
    for seq in record:
        platon_plasmid.append(seq.id)

with open("/home/tkosciuch/Results01180/platon/contigs.chromosome.fasta") as handle:
    record = list(SeqIO.parse(handle, "fasta"))
    for seq in record:
        platon_chromosome.append(seq.id)

#### plasforest

with open("/home/tkosciuch/Results01180/plasforest/plasforestResults.csv") as handle:
    



#### plasmidSPAdes

# create a blast database of SPAdes contigs
os.system("makeblastdb -in /output/Results/SPAdes/contigs.fasta -parse_seqids -dbtype nucl -out /output/Results/blast_db/SPAdes")

blastn_cline = NcbiblastnCommandline(query = "/output/Results/plasmidSPAdes/contigs.fasta", db = "/output/Results/blast_db/SPAdes", outfmt = 5, out = "/output/plasmidSPAdes/plasmidSPAdes_blast.xml") 

stdout, stderr = blastn_cline()

plasSPAdes_results = [["plasmidSPAdes plasmid","closest SPAdes contig"]]

for record in NCBIXML.parse(open("/output/plasmidSPAdes/plasmidSPAdes_blast.xml")): 
    if record.alignments:
        query = record.query.split("_component_")[0]
        match = record.alignments[0].title.split(" No definition line")[0]
        plasSPAdes_results.append([query,match])
        #results[record.query] = record.alignments[0].title

numpy.savetxt("/output/plasmidSPAdes_closest_conitg.csv", plasSPAdes_results, delimiter =", ", fmt ='% s')


#### combine platon and plasforest results
result = [["SPAdes contig", "platon","plasforest"]]
for contig in contigs:
    temp_result = []
    if contig in platon_plasmid:
        temp_result.append("plasmid")
    else if contig in platon_chromosome:
        temp_result.append("chromosome")
    else:
        temp_result.append("not evaluated")
    
    if contig in 

    
    
    result.append([contig,temp_result])