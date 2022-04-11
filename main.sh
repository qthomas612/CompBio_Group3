#!/bin/bash


#Take user input flags
while getopts t:s:r:d:o:p: flag
do
    case "${flag}" in
        t) threads=${OPTARG};;
        s) seqtype=${OPTARG};;
        r) trim=${OPTARG};;
        d) data=${OPTARG};;
        o) output=${OPTARG};;
        p) readtype=${OPTARG};;
       \?) echo "Error: Invalid option"
           exit;;
    esac
done

#set defaults if options are empty
${threads:-4}
${seqtype:-illumina}
${output:-./output}
${readtype:-unpaired}


#Make sure user input a data file, if not exit script
if [ -z "$data" ]; then
        echo 'Missing -d' >&2
        exit 1
fi

#If the user input a trim option then call trimmomatic
if $trim
then
  java -jar trimmomatic-0.35.jar SE -phred33 -d -o ILLUMINACLIP:TruSeq3-SE:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36
fi

#RUN THIS COMMAND WITH USER INPUTS
#SPADES ASSEMBLY
spades.py -s data/U54_LUC_01180.nanopore.fastq -o data/SpadesResults

#SPADES PLASMID PREDICTION


#PLASFOREST


#PLATON






