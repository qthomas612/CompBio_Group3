# CompBio_Group3

This program uses several plasmid identification tools to detect plasmid sequences from fastq files. Tools used include: spades, platon and plasforest.
Tools necessary for the use of this program can be accessed through the use of a dockerfile. All quality control of sequence reads should be done before using this pipeline.

Using the Dockerfile:
1. `wget https://github.com/qthomas612/CompBio_Group3/plasmid.py`
2. `python3 plasmid.py -t threads <-f your/file OR -1 forward/reads -2 reverse/reads> -o output/location -r readtype`
Using `python3 plasmid.py -h` will show a help file for the list of input flags

## Runtime
Expect a run time of about 30 to 50 min for using a paired reads file of 300mb using 16 threads.

## Command line options
``` 
python plasmid.py --help

optional arguments:
  -h, --help       show this help message and exit
  -t , --threads   number of CPUs to use in computation. Defaults to 4 threads
  -f , --file       input fasta or fastq file. Used only if the readtype flag is 12 or s
  -o , --output     directory to write results to
  -r , --readtype   Type of reads for SPAdes input. Options are 12, 1+2, or s. If 1+2, then the -1 and -2 flags must
                    be set
  -1 , --forward    forward read fasta or fastq file for SPAdes input. Used only if the readtype flag is 1+2
  -2 , --reverse    reverse read fasta or fastq file for SPAdes input.Used only if the readtype flag is 1+2
```
