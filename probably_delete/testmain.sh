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
#${threads:-4}
#${seqtype:-illumina}
#${output:-./output}
#${readtype:-unpaired}

echo $threads $seqtype $trim $data $output $readtype

if [ -z "$data" ]; then
        echo 'Missing -d' >&2
        exit 1
fi

#If the user input a trim option then call trimmomatic
if $trim
then
  echo $trim
fi
