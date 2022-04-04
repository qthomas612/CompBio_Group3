import os
##Theortical, do not attempt to use before extenstive bug fixing)
##This should start the docker and mount it. Will be etider later in order to have the mount lead to a drive on any users instead of hard coding
#docker exec must be used in order to run the commands from the docker container potientally a shell file ie .sh can be used instead
os.system("docker run --mount type=bind,source=/home/qthomas/data,target=/data -it plasmid:latest bash")
##Testing for plasforest
os.system("docker exec ./test_plasforest.sh")
##using plasforest
os.system("docker exec python3 PlasForest.py -i /data/U54_LUC_01180.nanopore.fastq")
#Using Platon
##platon database should be set up upon creation of the container
#!Alert results need to be changed to allow output from docker container to the users output.
os.system("docker exec platon --db ~/db --output results/ --verbose  /data/U54_LUC_01180.nanopore.fastq")
#Need to address if we are using SPAdes or plasmidSPAdes for input into recycler before wiritng the code to do it
