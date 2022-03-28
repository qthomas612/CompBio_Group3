# CompBio_Group3

This program uses several plasmid identification tools to detect plasmid sequences from fastq files. Tools used include: spades, recycler, platon and plasforest.
Tools necessary for the use of this program can be accessed through the use of a dockerfile.

Using the Dockerfile:
1. git clone 
2. docker build -t plasmid .
3. The docker container with the databases can be accessed by running:
  docker run -it plasmid:latest bash
  
Test docker build:
  python3 test_installation.py
  
