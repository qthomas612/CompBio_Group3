#!/bin/bash


#Take user input flags
while getopts t:s:r:d:o:p: flag
do
    case "${flag}" in
        t) threads=${OPTARG};;
        s) seqtype=${OPTARG};;
        r) trim=${OPTARG};;
        d) data=${OPTARG};;
        p) readtype=${OPTARG};;
       \?) echo "Error: Invalid option"
           exit;;
    esac
done

## TK: couldn't get the defaults to work here and defaults are handled in plasmid.py
#set defaults if options are empty
#${threads:-4}
#${seqtype:-illumina}
#${output:-./output}
#${readtype:-unpaired}

## TK: will check this in plasmid.py
#Make sure user input a data file, if not exit script
#if [ -z "$data" ]; then
#        echo 'Missing -d' >&2
#        exit 1
#fi

#If the user input a trim option then call trimmomatic
if $trim
then
  java -jar trimmomatic-0.35.jar SE -phred33 -d -o ILLUMINACLIP:TruSeq3-SE:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36
fi

#RUN THIS COMMAND WITH USER INPUTS
#SPADES ASSEMBLY
spades.py -s data/$data -o /output/SpadesResults

#SPADES PLASMID PREDICTION
#double check this command is right || Command is right and runs without errors
spades.py --plasmid -s data/$data -o data/SpadesResults

#PLASFOREST
python3 PlasForest.py -i /data/SpadesResult/contigs.fasta

#PLATON
platon --db ~/db --output ./spades_test/ --verbose --threads 8 ./SpadesResult/contigs.fasta


#RECYCLER
conda activate recycler
make_fasta_from_fastg.py -g ./data/SpadesResults/assembly_graph.fastg [-o assembly_graph.nodes.fasta]
bwa index assembly_graph.nodes.fasta
bwa mem assembly_graph.nodes.fasta R1.fastq.gz R2.fastq.gz | samtools view -buS - > reads_pe.bam
samtools view -bF 0x0800 reads_pe.bam > reads_pe_primary.bam
samtools sort reads_pe_primary.bam reads_pe_primary.sort.bam
samtools index reads_pe_primary.sort.bam

recycle.py -g ./spades_test/assembly_graph.fastg -k 55 -b reads_pe_primary.sort.bam -i True



