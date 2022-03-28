# CompBio_Group3

This program uses several plasmid identification tools to detect plasmid sequences from fastq files. Tools used include: spades, recycler, platon and plasforest.

Using the Dockerfile:
1. git clone 
2. docker build -t plasmid .
3. The docker container without databases can be accessed by running:
  docker run -it plasmid:nodb bash
4. The docker container with the databases can be accessed by running:
  docker run -it plasmid:latest bash 
