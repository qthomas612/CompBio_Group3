#!/usr/bin/python3

import os, argparse, multiprocessing

ap = argparse.ArgumentParser()
ap.add_argument('-t','--threads', type = int, default = 4, help = 'Number of CPUs to use in computation. Defaults to half the number of available CPUs', metavar = '')
ap.add_argument('-s','--seqtype', type = str, default = "illumina", help = 'Type of sequences. Options are illumina or nanopore. The illumina option works for all short reads', metavar = '')
ap.add_argument('-d','--data', type = str, required = True,  help = 'input data', metavar = '')
ap.add_argument('-o','--output', type = str, default = "./output", help = 'directory to write results to', metavar = '')
ap.add_argument('-l','--readtype', type = str, default = False, help = "Type of reads. Options are 'interlaced forward', 'reverse paired-end', or 'forward paired-end'", metavar = '')

args = vars(ap.parse_args())

assert os.path.isfile(args['data']), "Could not find the file {}".format(args['data'])

os.makedirs(args['output'],exist_ok = True)

data =  os.path.realpath(args['data'])
data_target = os.path.basename(args['data'])
output = os.path.realpath(args['output'])

docker_str = "docker run --mount type=bind,source="+data+",target=/data/"+data_target+" --mount type=bind,source="+output+",target=/output plasmid:latest -t "+str(args['threads'])+" -s "+args["seqtype"]+" -d "+data_target

if args['trim']:
    docker_str += " -r "+args['trim']

print(docker_str)
