# CompBio_Group3

This program uses several plasmid identification tools to detect plasmid sequences from fastq files. Tools used include: spades, platon and plasforest.
Tools necessary for the use of this program can be accessed through the use of a dockerfile. All quality control of sequence reads should be done before using this pipeline.

Using the Dockerfile:
1. `git clone` 
2. `docker build -t plasmid .`
3. `python3 plasmid.py -f your/file -o output/location -r readtype_of_input`
Using `plasmid.py -h` can show a help file for the list of input flags`
Test docker build:

  `python3 test_installation.py`

For ease of using the program, plasmid.py is a python wrapper for `docker run`

## Runtime
Expect a run time of about 30 to 50 min for using a paired reads file of 300mb using 16 threads.

## Command line options
``` 
python plasmid.py --help

optional arguments:
  -h, --help       show this help message and exit
  -t , --threads   Number of CPUs to use in computation. Defaults to half the number of available CPUs
  -f , --file      path to input data
  -o , --output    directory to write results to
  -r , --readtype   Type of reads. Options are 'interlaced forward', 'reverse paired-end', or 'forward paired-end'
  -1 , --forward    Path to forward read fastq file. Used only if the readtype flag is 1+2.
  -2 , --reverse    Path to reverse read fastq file. Used only if the readtype flag is 1+2.
```

```docker logs <container id>``` will show the commands running in the container and any error messages
