#!/bin/bash

cd /root

# miniconda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ./miniconda.sh
chmod 755 miniconda.sh
./miniconda.sh -b -p /root/miniconda
conda init bash
source /root/.profile
rm miniconda.sh

# spades 3.15.4
wget https://cab.spbu.ru/files/release3.15.4/SPAdes-3.15.4-Linux.tar.gz
tar -xzf SPAdes-3.15.4-Linux.tar.gz
rm SPAdes-3.15.4-Linux.tar.gz

# recycler. recycler is built in python 2.7 so create a seperate conda env for it
#conda create -n recycler -y python=2.7
#conda activate recycler
#conda install -c bioconda recycler
#conda activate base

# recycler. recycler is built in python 2.7 so create a seperate conda env for it
conda create -n recycler -y python=2.7
conda activate recycler
wget https://github.com/Shamir-Lab/Recycler/releases/download/v0.7/Recycler-v0.7.zip
chmod 755 Recycler-v0.7.zip
unzip Recycler-v0.7.zip
rm Recycler-v0.7.zip
chmod 755 -R ./Recycler-0.7
cd Recycler-0.7
python setup.py install --user
cd /root
conda activate base

# samtools
wget https://github.com/samtools/samtools/releases/download/1.15/samtools-1.15.tar.bz2
chmod 755 samtools-1.15.tar.bz2
tar -xf samtools-1.15.tar.bz2
rm samtools-1.15.tar.bz2
chmod 755 -R ./samtools-1.15
cd samtools-1.15
make
make install
cd /root

# Trimmomatic
conda install -c bioconda trimmomatic

# bwa
wget https://sourceforge.net/projects/bio-bwa/files/bwa-0.7.17.tar.bz2
chmod 755 bwa-0.7.17.tar.bz2
tar -xvf bwa-0.7.17.tar.bz2
rm bwa-0.7.17.tar.bz2
chmod 755 -R ./bwa-0.7.17
cd bwa-0.7.17
make
cd /root

# platon
conda install -c conda-forge -c bioconda -c defaults -y platon

# plasforest
conda install -y -c anaconda -c conda-forge biopython scikit-learn numpy pandas joblib
git clone https://github.com/leaemiliepradier/PlasForest
chmod 755 -R ./PlasForest
cd PlasForest
tar -zxvf plasforest.sav.tar.gz
rm plasforest.sav.tar.gz
sed -i 's:input("Do you want to download them? (y/n) "):"y":g' check_and_download_database.py

#BioPython, scikit-learn 0.22.2.post1, Numpy, Pandas, Joblib
#conda install numpy
#conda install pandas
#conda install -c conda-forge joblib
#conda install scikit-learn
#conda install -c conda-forge biopython

source /root/.profile
