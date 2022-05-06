#!/usr/bin/python3

import os, argparse, multiprocessing
##Reads in arguments from user for flags needed in the pipeline
ap = argparse.ArgumentParser()
ap.add_argument('-t','--threads', type = int, default = 4, help = 'number of CPUs to use in computation. Defaults to 4 threads', metavar = '')
ap.add_argument('-f','--file', type = str, required = False,  help = 'input fasta or fastq file. Used only if the readtype flag is 12 or s', metavar = '')
ap.add_argument('-o','--output', type = str, default = "./output", help = 'directory to write results to. Defaults to ./output', metavar = '')
ap.add_argument('-r','--readtype', type = str, required = False, help = "type of reads for SPAdes input. Options are 12, 1+2, or s. If 1+2, then the -1 and -2 flags must be set", metavar = '')
ap.add_argument('-1','--forward', type = str, required = False, help = "forward read fasta or fastq file for SPAdes input. Used only if the readtype flag is 1+2", metavar = '')
ap.add_argument('-2','--reverse', type = str, required = False, help = "reverse read fasta or fastq file for SPAdes input. Used only if the readtype flag is 1+2", metavar = '')

args = vars(ap.parse_args())

os.makedirs(args['output'],exist_ok = False)
output = os.path.realpath(args['output'])
##Sets up the correct docker string based on the readtype input of 12 or s
if args["readtype"] in ["12","s"]:
    assert os.path.isfile(args['file']), "Could not find the file {}".format(args['file'])
    data =  os.path.realpath(args['file'])
    data_target = os.path.basename(args['file'])
    docker_str = "docker run --mount type=bind,source="+data+",target=/data/"+data_target+" --mount type=bind,source="+output+",target=/output triskos/plasmid-id:latest /usr/local/bin/main.sh -t "+str(args['threads'])+" -r "+args["readtype"]+" -f "+data_target
##Sets up the correct docker string based on the readtype input of 1+2
if args["readtype"] == "1+2":
    assert os.path.isfile(args['forward']), "Could not find the file {}".format(args['file'])
    assert os.path.isfile(args['reverse']), "Could not find the file {}".format(args['file'])
    forward =  os.path.realpath(args['forward'])
    forward_target = os.path.basename(args['forward'])
    reverse =  os.path.realpath(args['reverse'])
    reverse_target = os.path.basename(args['reverse'])
    docker_str = "docker run --mount type=bind,source="+forward+",target=/data/"+forward_target+" --mount type=bind,source="+reverse+",target=/data/"+reverse_target+" --mount type=bind,source="+output+",target=/output triskos/plasmid-id:latest /usr/local/bin/main.sh -t "+str(args['threads'])+" -r "+args["readtype"]+" -1 "+forward_target+ " -2 "+reverse_target
#Starts the docker
os.system(docker_str)
