import os
##Theortical, do not attempt to use before extenstive bug fixing)




#Trimmomatic


#Need to run spades first
os.system("spades.py -s data/U54_LUC_01180.nanopore.fastq -o data/SpadesResults")
##Testing for plasforest
os.system("./test_plasforest.sh")
##using plasforest
os.system("python3 PlasForest.py -i /data/")
#Using Platon
##platon database should be set up upon creation of the container
#!Alert results need to be changed to allow output from docker container to the users output.
os.system("docker exec platon --db ~/db --output results/ --verbose  /data/U54_LUC_01180.nanopore.fastq")
#Need to address if we are using SPAdes or plasmidSPAdes for input into recycler before wiritng the code to do it
