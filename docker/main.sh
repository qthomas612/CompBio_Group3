#!/bin/bash


#Take user input flags
while getopts t:r:d:1:2: flag
do
    case "${flag}" in
        t) threads=${OPTARG};;
        f) file=${OPTARG};;
        r) readtype=${OPTARG};;
        1) forward=${OPTARG};;
        2) reverseto=${OPTARG};;
       \?) echo "Error: Invalid option"
           exit;;
    esac
done

#make output directory of results
mkdir ./output/Results ./output/Results/blast_db ./output/Results/plasforest ./output/Results/platon ./output/Results/SPAdes ./output/Results/plasmidSPAdes

#SPADES ASSEMBLY
if [$readtype = "12"]
then
    spades.py -t $threads --12 ./data/$file -o ./output/Results/SPAdes
elif [$readtype = "1+2"]
then
    spades.py -t $threads -1 ./data/$1 -2 ./data/$2 -o ./output/Results/SPAdes
else
    spades.py -t $threads -$readtype ./data/$file -o ./output/Results/SPAdes
fi

#SPADES PLASMID PREDICTION
#double check this command is right || Command is right and runs without errors
#spades.py --plasmid -s /data/$data -o /output/Results/plasmidSPAdes

if [$readtype = "12"]
then
    spades.py -t $threads --plasmid --12 ./data/$file -o ./output/Results/plasmidSPAdes
elif [$readtype = "1+2"]
then
    spades.py -t $threads --plasmid -1 ./data/$1 -2 ./data/$2 -o ./output/Results/plasmidSPAdes
else
    spades.py -t $threads --plasmid -$readtype ./data/$file -o ./output/Results/plasmidSPAdes
fi

#PLASFOREST
#plasforest app has all the paths to needed files hardcoded in their main file so redirect to PlasForest directory and return after using it.
#run plasForest
cd /root/PlasForest
PlasForest.py --threads $threads -i ./output/Results/SPAdes/contigs.fasta  -o ./output/Results/plasforest/plasforestResults.csv
cd

#return to previous directory
#cd ../../ # TK: I don't think we need to move around directories as all the tools should be in $PATH

#PLATON
platon --threads $threads --db ~/db --output ./output/Results/platon/ ./output/Results/SPAdes/contigs.fasta

# format results
/root/compile_results.py

#RECYCLER # TK: commented out bc its not currently working
#conda activate recycler
#make_fasta_from_fastg.py -g /output/SpadesResults/assembly_graph.fastg -o /output/recycler/assembly_graph.nodes.fasta
#bwa index /output/recycler/assembly_graph.nodes.fasta
#bwa mem /output/recycler/assembly_graph.nodes.fasta /output/recycler/R1.fastq.gz /output/recycler/R2.fastq.gz | samtools view -buS - > /output/recycler/reads_pe.bam
#samtools view -bF 0x0800 /output/recycler/reads_pe.bam > /output/recycler/reads_pe_primary.bam
#samtools sort /output/recycler/reads_pe_primary.bam -o /output/recycler/reads_pe_primary.sort.bam
#samtools index /output/recycler/reads_pe_primary.sort.bam

# find largest kmer used by spades


#recycle.py -g /output/recycler/assembly_graph.fastg -k 55 -b /output/recycler/reads_pe_primary.sort.bam -i True -o /output/recycler/
# need to figure out what spades used for k value
#SPAdes utilizes multisized de Bruijn graph which allows employing different values of k. That is what the K<##> in resutls related to, so we have no set k-value


