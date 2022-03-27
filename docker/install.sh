#!/bin/bash

## The databases for platon and plasforest are commented out for time while debugging

cd /root

# miniconda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ./miniconda.sh
chmod 755 miniconda.sh
./miniconda.sh -b -p /root/miniconda


# spades 3.15.4
wget https://cab.spbu.ru/files/release3.15.4/SPAdes-3.15.4-Linux.tar.gz
tar -xzf SPAdes-3.15.4-Linux.tar.gz
rm SPAdes-3.15.4-Linux.tar.gz

# recycler. recycler is built in python 2.7 so create a seperate conda env for it
conda create -n recycler -y python=2.7
conda activate recycler
wget https://github.com/Shamir-Lab/Recycler/releases/download/v0.7/Recycler-v0.7.zip
chmod 755 Recycler-v0.7.zip
unzip Recycler-v0.7.zip
cd Recycler-0.7
python3 setup.py install --user
cd /root

conda activate base

# samtools
wget https://github.com/samtools/samtools/releases/download/1.15/samtools-1.15.tar.bz2
chmod 755 samtools-1.15.tar.bz2
tar -xf samtools-1.15.tar.bz2
cd samtools-1.15
make
make install
cd /root

# platon
conda install -c conda-forge -c bioconda -c defaults -y platon
#wget https://zenodo.org/record/4066768/files/db.tar.gz
#chmod 755 db.tar.gz
#tar -xzf db.tar.gz
#rm db.tar.gz

# plasforest
git clone https://github.com/leaemiliepradier/PlasForest
cd PlasForest
tar -zxvf plasforest.sav.tar.gz
chmod 755 database_downloader.sh
#./database_downloader.sh
