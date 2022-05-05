#!/bin/bash


#Take user input flags
while getopts t:r:f:1:2: flag
do
    case "${flag}" in
        t) threads=${OPTARG};;
        f) file=${OPTARG};;
        r) readtype=${OPTARG};;
        1) forward=${OPTARG};;
        2) reverse=${OPTARG};;
       \?) echo "Error: Invalid option"
           exit;;
    esac
done
cd /
#make output directory of results
mkdir /output/blast_db /output/plasforest /output/platon /output/SPAdes /output/plasmidSPAdes

#SPADES ASSEMBLY
if [ $readtype = "12" ]
then
    spades.py -t $threads --12 ./data/$file -o ./output/SPAdes
elif [ $readtype = "1+2" ]
then
    spades.py -t $threads -1 ./data/$forward -2 ./data/$reverse -o ./output/SPAdes
elif [ $readtype = "s" ]
    spades.py -t $threads -$readtype ./data/$file -o ./output/SPAdes
fi

#SPADES PLASMID PREDICTION
#double check this command is right || Command is right and runs without errors
#spades.py --plasmid -s /data/$data -o /output/plasmidSPAdes

if [ $readtype = "12" ]
then
    spades.py -t $threads --plasmid --12 ./data/$file -o ./output/plasmidSPAdes
elif [ $readtype = "1+2" ]
then
    spades.py -t $threads --plasmid -1 ./data/$forward -2 ./data/$reverse -o ./output/plasmidSPAdes
elif [ $readtype = "s" ]
    spades.py -t $threads --plasmid -$readtype ./data/$file -o ./output/plasmidSPAdes
fi

#PLASFOREST
#plasforest app has all the paths to needed files hardcoded in their main file so redirect to PlasForest directory and return after using it.
#run plasForest
cd /root/PlasForest
PlasForest.py --threads $threads -i /output/SPAdes/contigs.fasta  -o /output/plasforest/plasforestResults.csv
cd /

#return to previous directory
#cd ../../ # TK: I don't think we need to move around directories as all the tools should be in $PATH

#PLATON
platon --threads $threads --db ~/db --output /output/platon/ /output/SPAdes/contigs.fasta

# format results
python3 /root/compile_results.py



