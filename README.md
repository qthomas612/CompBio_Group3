# CompBio_Group3

Using the Dockerfile:
1. git clone 
2. docker build -t "proj:Dockerfile" .
3. The docker container without databases can be accessed by running:
  docker run -it plasmid:nodb bash
4. The docker container with the databases can be accessed by running:
  docker run -it plasmid:latest bash 
