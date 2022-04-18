import os
##Theortical, do not attempt to use before extenstive bug fixing)

import os, argparse, multiprocessing

ap = argparse.ArgumentParser()
ap.add_argument('-t','--threads', type = int, default = multiprocessing.cpu_count()/2, help = 'Number of CPUs to use in computation. Defaults to half the number of available CPUs', metavar = '')
ap.add_argument('-s','--seqtype', type = str, default = "illumina", help = 'Type of sequences. Options are illumina or nanopore. The illumina option works for all short reads', metavar = '')
ap.add_argument('-r','--trim', type = str, default = False, help = 'Trim adapter sequences using trimmomatic. Accpets a string of the adapter to trim', metavar = '')
ap.add_argument('-d','--data', type = str, required = True,  help = 'input data', metavar = '')
ap.add_argument('-o','--output', type = str, default = "./output", help = 'directory to write results to', metavar = '')
ap.add_argument('-1','--readtype', type = str, default = "unpaired", help = 'Type of reads. Options are interlaced forward and reverse paired-end reads, forward paired-end reads, file with reverse paired-end reads, file with unpaired reads' metavar = '')

args = vars(ap.parse_args())

assert os.path.isfile(args['data']), "Could not find the file {}".format(args['data'])


#Trimmomatic
#if -r == True:
    #os.system(java -jar trimmomatic-0.35.jar SE -phred33 -d -o ILLUMINACLIP:TruSeq3-SE:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36)



#Need to run spades first
os.system("spades.py -s data/U54_LUC_01180.nanopore.fastq -o data/SpadesResults")
##os.system("spades.py -s [data] -o args[output]")
#if args[readtype] != "unpaired":
    #if args[readtype] == "forward and reverse paired-end"
        #os.system("spades.py -12 [data] -o args[output]")
    #if args[readtype] == "forward paired-end"
            #os.system("spades.py -1 [data] -o args[output]")
    #if args[readtype] == "reverse paired-end"
            #os.system("spades.py -2 [data] -o args[output]")
#Run Plasmidspades                   
##Testing for plasforest
#os.system("./test_plasforest.sh")
##using plasforest
os.system("python3 PlasForest.py -i /data/SpadesResult/contigs.fasta")
#Using Platon
##platon database should be set up upon creation of the container
#!Alert results need to be changed to allow output from docker container to the users output.
#os.system("docker exec platon --db ~/db --output results/ --verbose  "+ "args[output]" + "/contigs.fasta")
os.system("docker exec platon --db ~/db --output results/ --verbose  /data/SpadesResult/contigs.fasta")

                
                
                
##Recycler
os.system("make_fasta_from_fastg.py -g ./data/SpadesResult/assembly_graph.fastg [-o assembly_graph.nodes.fasta]")             
os.system("bwa index assembly_graph.nodes.fasta")
os.system("bwa mem assembly_graph.nodes.fasta R1.fastq.gz R2.fastq.gz | samtools view -buS - > reads_pe.bam")                
os.system("samtools view -bF 0x0800 reads_pe.bam > reads_pe_primary.bam")
os.system("samtools sort reads_pe_primary.bam reads_pe_primary.sort.bam")
os.system("samtools index reads_pe_primary.sort.bam")
                
os.system("recycle.py -g ./spades_test/assembly_graph.fastg -k 55 -b reads_pe_primary.sort.bam -i True")
                
#PLATON
os.system("platon --db ~/db --output ./spades_test/ --verbose --threads 8 ./SpadesResult.contigs.fasta")                
                
                
