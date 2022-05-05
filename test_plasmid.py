#!/usr/bin/python3

import os, argparse, multiprocessing

ap = argparse.ArgumentParser()
ap.add_argument('-t','--threads', type = int, default = 4, help = 'Number of CPUs to use in computation. Defaults to half the number of available CPUs', metavar = '')
ap.add_argument('-f','--file', type = str, required = False,  help = 'input fasta or fastq file. Used only if the readtype flag is 12 or s', metavar = '')
ap.add_argument('-o','--output', type = str, default = "./output", help = 'directory to write results to', metavar = '')
ap.add_argument('-r','--readtype', type = str, required = False, help = "Type of reads for spades input. Options are 12, 1+2, or s. If 1+2, then the -1 and -2 flags must be set", metavar = '')
ap.add_argument('-1','--forward', type = str, required = False, help = "forward read fasta or fastq file for spades input. Used only if the readtype flag is 1+2", metavar = '')
ap.add_argument('-2','--reverse', type = str, required = False, help = "reverse read fasta or fastq file for spades input.Used only if the readtype flag is 1+2", metavar = '')
ap.add_argument('-m','--main', type = str, required = False, help = "path to local main.sh", metavar = '')


args = vars(ap.parse_args())

output = os.path.realpath(args['output'])
os.makedirs(args['output'],exist_ok = True)
mainsh =  os.path.realpath(args['main'])
mainsh_target = os.path.basename(args['main'])

if args["readtype"] in ["12","s"]:
    assert os.path.isfile(args['file']), "Could not find the file {}".format(args['file'])
    data =  os.path.realpath(args['file'])
    data_target = os.path.basename(args['file'])
    docker_str = "docker run --rm --mount type=bind,source="+mainsh+",target=/data/"+mainsh_target+" --mount type=bind,source="+data+",target=/data/"+data_target+" --mount type=bind,source="+output+",target=/output plasmid:latest /data/main.sh -t "+str(args['threads'])+" -r "+args["readtype"]+" -f "+data_target

if args["readtype"] == "1+2":
    assert os.path.isfile(args['forward']), "Could not find the file {}".format(args['file'])
    assert os.path.isfile(args['reverse']), "Could not find the file {}".format(args['file'])
    forward =  os.path.realpath(args['forward'])
    forward_target = os.path.basename(args['forward'])
    reverse =  os.path.realpath(args['reverse'])
    reverse_target = os.path.basename(args['reverse'])
    docker_str = "docker run --rm --mount type=bind,source="+mainsh+",target=/data/"+mainsh_target+" --mount type=bind,source="+forward+",target=/data/"+forward_target+" --mount type=bind,source="+reverse+",target=/data/"+reverse_target+" --mount type=bind,source="+output+",target=/output plasmid:latest /data/main.sh -t "+str(args['threads'])+" -r "+args["readtype"]+" -1 "+forward_target+ " -2 "+reverse_target

os.system(docker_str)
