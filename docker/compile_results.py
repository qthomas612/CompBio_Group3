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
# with open("/home/tkosciuch/Results01180/SPAdes/contigs.fasta") as handle:
#     record = list(SeqIO.parse(handle, "fasta"))
#     for seq in record:
#         contigs.append(seq.id)

#### platon
# "/home/tkosciuch/Results01180/platon/contigs.plasmid.fasta"
platon_plasmid = []
platon_chromosome = []

with open("/output/platon/contigs.plasmid.fasta") as handle:
    record = list(SeqIO.parse(handle, "fasta"))
    for seq in record:
        platon_plasmid.append(seq.id)

with open("/output/platon/contigs.chromosome.fasta") as handle:
    record = list(SeqIO.parse(handle, "fasta"))
    for seq in record:
        platon_chromosome.append(seq.id)

#### plasforest
plasforest_plasmid = []
plasforest_chromosome = []

with open("/output/plasforest/plasforestResults.csv") as handle:
    input = handle.readlines()
    for contig in input:
        temp_contig = contig.split(",")
        if temp_contig[1].strip() == "Plasmid":
            plasforest_plasmid.append(temp_contig[0])
        elif temp_contig[1].strip() == "Chromosome":
            plasforest_chromosome.append(temp_contig[0])


#### combine platon and plasforest results
result = [["SPAdes contig", "platon","plasforest"]]
for contig in contigs:
    temp_result = [contig]
    if contig in platon_plasmid:
        temp_result.append("plasmid")
    elif contig in platon_chromosome:
        temp_result.append("chromosome")
    else:
        temp_result.append("not evaluated")
    
    if contig in plasforest_plasmid:
        temp_result.append("plasmid")
    elif contig in plasforest_chromosome:
        temp_result.append("chromosome")
    else:
        temp_result.append("not evaluated")
    result.append(temp_result)

numpy.savetxt("/output/plasforest_platon.csv", result, delimiter =", ", fmt ='% s')

#### plasmidSPAdes, perform BLASTN on SPAdes contig.fasta

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

