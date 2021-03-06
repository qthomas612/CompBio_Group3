# CompBio_Group3

This program uses several plasmid identification tools to detect plasmid sequences from fastq files. Tools used include: SPAdes, platon and plasForest. SPAdes is used to align reads into contigs, and then platon and plasforest classify contigs as plasmid or chromosome. SPAdes is run a seperate time using the `--plasmid` flag to detect plasmids. The SPAdes plasmids are matched to the original SPAdes contigs by a local BLASTN.
  
All quality control of sequence reads should be done before using this pipeline.

## Requirements
  
Python3  
Docker
  
## Using the program
  
1. `wget https://raw.githubusercontent.com/qthomas612/CompBio_Group3/main/plasmid.py`
2. `python3 plasmid.py -t threads <-f your/file OR -1 forward/reads -2 reverse/reads> -o output/location -r readtype`

## Example Data

E. coli practice data can be downloaded at https://www.ncbi.nlm.nih.gov/sra/SRX13373163[accn]. 
Alternatively you can download with SRA-toolkit using the commands:
1. `prefetch SRR17191338`
2. `fasterq-dump --split-files SRR17191338/SRR17191338.sra`

## Example usage
`python3 plasmid.py -t 16 -r 1+2 -1 SRR17191338_1.fastq -2 SRR17191338_2.fastq`
  
Expect this example to finish in about 40 minutes using 16 threads. More time will be needed to pull the docker image if this is the first time plasmid.py is being used.

## Command line options
``` 
python3 plasmid.py --help

optional arguments:
  -h, --help        show this help message and exit
  -t , --threads    number of CPUs to use in computation. Defaults to 4 threads
  -f , --file       input fasta or fastq file. Used only if the readtype flag is 12 or s
  -r , --readtype   type of reads for SPAdes input. Options are 12, 1+2, or s. If 1+2, then the -1 and -2 flags must
                    be set
  -1 , --forward    forward read fasta or fastq file for SPAdes input. Used only if the readtype flag is 1+2
  -2 , --reverse    reverse read fasta or fastq file for SPAdes input. Used only if the readtype flag is 1+2
```

## Output

This program creates a folder named output that contains all files produced by the pipeline. There are three output files produced independent of the individual tools to evaluate plasmid prediction across programs. The first is "results.csv" in which all SPAdes contigs are listed with the chromosomal/plasmid prediction of each tool for that contig. The second is "plasmidSPAdes_closest_conitg.csv" which has each plasmidSPAdes contig and the corresponding SPAdes match along with the escore and bit score for that match. The last is "summary_results.txt" which contains a summary of the number of plasmids each tool identified as well as the number of overlap between tools. You can find output of individual tools in their corresponding output folder. 
