Import OS
##This should start the docker and mount it. Will be etider later in order to have the mount lead to a drive on any users instead of hard coding
os.system("docker run --mount type=bind,source=/home/qthomas/data,target=/data -it plasmid:latest bash")
##Testing for plasforest
os.system("docker exec ./test_plasforest.sh")
##using plasforest
os.system("docker exec python3 PlasForest.py -i data/")

