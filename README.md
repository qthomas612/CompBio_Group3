# CompBio_Group3

This program uses several plasmid identification tools to detect plasmid sequences from fastq files. Tools used include: spades, recycler, platon and plasforest.
Tools necessary for the use of this program can be accessed through the use of a dockerfile.

Using the Dockerfile:
1. `git clone` 
2. `docker build -t plasmid .`
3. The docker container with the databases can be accessed by running:
  `docker run --rm --mount type=bind,source=/home/qthomas/data,target=/data -it plasmid:noentrypoint bash`
    - when writing to /data in the docker container, those files will also be written to /home/qthomas/data.
    - multiple folders can be bound i.e. `docker run --rm --mount type=bind,source=/home/qthomas/data,target=/data --mount type=bind,source=/home/qthomas/results,target=/results -it plasmid:noentrypoint bash`

Test docker build:

  `python3 test_installation.py`

For ease of using the program, plasmid.py is a python wrapper for `docker run`

## Command line options
``` 
python plasmid.py --help

optional arguments:
  -h, --help       show this help message and exit
  -t , --threads   Number of CPUs to use in computation. Defaults to half the number of available CPUs
  -s , --seqtype   Type of sequences. Options are illumina or nanopore. The illumina option works for
                   all short reads
  -r , --trim      Trim adapter sequences using trimmomatic. Accpets a string of the adapter to trim
  -d , --data      input data
  -o , --output    directory to write results to
  -l , --readtype   Type of reads. Options are 'interlaced forward', 'reverse paired-end', or 'forward paired-end'
```
