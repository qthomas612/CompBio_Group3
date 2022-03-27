#!/bin/bash

cd /root

# platon
wget https://zenodo.org/record/4066768/files/db.tar.gz
chmod 755 db.tar.gz
tar -xzf db.tar.gz
rm db.tar.gz

# plasforest
cd PlasForest
./database_downloader.sh
