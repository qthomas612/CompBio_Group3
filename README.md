# CompBio_Group3

This program uses several plasmid identification tools to detect plasmid sequences from fastq files. Tools used include: spades, platon and plasforest. SPAdes is used to align reads into contigs, and then platon and plasforest classify contigs as plasmid or chromosome. SPAdes is run a seperate time using the `--plasmid` flag to detect plasmids. The SPAdes plasmids are matched to the original SPAdes contigs by a local BLASTN.
  
All quality control of sequence reads should be done before using this pipeline.
  
## Using the program
  
1. `wget https://raw.githubusercontent.com/qthomas612/CompBio_Group3/main/plasmid.py`
2. `python3 plasmid.py -t threads <-f your/file OR -1 forward/reads -2 reverse/reads> -o output/location -r readtype`

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
  -o , --output     directory to write results to, defaults to ./output
  -r , --readtype   type of reads for SPAdes input. Options are 12, 1+2, or s. If 1+2, then the -1 and -2 flags must
                    be set
  -1 , --forward    forward read fasta or fastq file for SPAdes input. Used only if the readtype flag is 1+2
  -2 , --reverse    reverse read fasta or fastq file for SPAdes input. Used only if the readtype flag is 1+2
```
