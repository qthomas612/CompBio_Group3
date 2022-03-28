#We could use this to make sure that the docker file not only installed all the dependencies, but also that everything work
#Only thought to include this because even though I have spades properly installed the spades.py --test fails.

import os

#first we must test SPADES as this is a requirement for many of the other programs
wd = os.getcwd()
os.system("spades.py --test > spadestest.log")
spadesresults = wd + "/spades_test/"


#Next we can test recycler. For this we need the graph and a bam file. Let's start with the bamFile
#Following recycler installation page...
os.system("make_fasta_from_fastg.py -g assembly_graph.fastg [-o assembly_graph.nodes.fasta]")
os.system("bwa index assembly_graph.nodes.fasta")
os.system("bwa mem assembly_graph.nodes.fasta R1.fastq.gz R2.fastq.gz | samtools view -buS - > reads_pe.bam")
os.system("samtools view -bF 0x0800 reads_pe.bam > reads_pe_primary.bam")
os.system("samtools sort reads_pe_primary.bam reads_pe_primary.sort.bam")
os.system("samtools index reads_pe_primary.sort.bam")

#etc etc
