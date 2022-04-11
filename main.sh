#!/bin/bash

while getopts t:s:r:d:o:p: flag
do
    case "${flag}" in
        t) threads=${OPTARG};;
        s) seqtype=${OPTARG};;
        r) trim=${OPTARG};;
        d) data=${OPTARG};;
        o) output=${OPTARG};;
        p) readtype=${OPTARG};;
    esac
done


spades.py -s data/U54_LUC_01180.nanopore.fastq -o data/SpadesResults






