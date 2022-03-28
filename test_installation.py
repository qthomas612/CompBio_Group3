#We could use this to make sure that the docker file not only installed all the dependencies, but also that everything work
#Only thought to include this because even though I have spades properly installed the spades.py --test fails.

import os

#SPADES test
wd = os.getcwd()
os.system("spades.py --test > spadestest.log")
spadesresults = wd + "/spades_test/"


#RECYCLER TEST 
#For this we need the graph and a bam file. Let's start with the bamFile
os.system("conda activate recycler")
os.system("make_fasta_from_fastg.py -g ./spades_test/assembly_graph.fastg [-o assembly_graph.nodes.fasta]")
os.system("bwa index assembly_graph.nodes.fasta")
os.system("bwa mem assembly_graph.nodes.fasta R1.fastq.gz R2.fastq.gz | samtools view -buS - > reads_pe.bam")
os.system("samtools view -bF 0x0800 reads_pe.bam > reads_pe_primary.bam")
os.system("samtools sort reads_pe_primary.bam reads_pe_primary.sort.bam")
os.system("samtools index reads_pe_primary.sort.bam")

os.system("recycle.py -g ./spades_test/assembly_graph.fastg -k 55 -b reads_pe_primary.sort.bam -i True")
os.system("conda deactivate")

#platon
os.system()

#plasforest
 


#lol why did I not make this a shell script
#etc etc
