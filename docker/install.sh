#!/bin/bash

cd /root

# miniconda
wget -nv https://repo.anaconda.com/miniconda/Miniconda3-py37_4.11.0-Linux-x86_64.sh -O ./miniconda.sh
chmod 755 miniconda.sh
./miniconda.sh -b -p /root/miniconda
conda init bash
source /root/.profile
source /root/miniconda/etc/profile.d/conda.sh
rm miniconda.sh

# spades 3.15.4
wget -nv https://cab.spbu.ru/files/release3.15.4/SPAdes-3.15.4-Linux.tar.gz
tar -xzf SPAdes-3.15.4-Linux.tar.gz
rm SPAdes-3.15.4-Linux.tar.gz

# samtools
wget -nv https://github.com/samtools/samtools/releases/download/1.15/samtools-1.15.tar.bz2
chmod 755 samtools-1.15.tar.bz2
tar -xf samtools-1.15.tar.bz2
rm samtools-1.15.tar.bz2
chmod 755 -R ./samtools-1.15
cd samtools-1.15
make
make install
cd /root

# platon
conda install -c conda-forge -c bioconda -c defaults -y platon

# plasforest
conda install -y -c anaconda -c conda-forge biopython scikit-learn==0.22.2.post1 numpy pandas joblib
git clone https://github.com/leaemiliepradier/PlasForest
chmod 755 -R ./PlasForest
cd PlasForest
tar -zxvf plasforest.sav.tar.gz
rm plasforest.sav.tar.gz
sed -i 's|input("Do you want to download them? (y/n) ")|"y"|g' check_and_download_database.py
sed -i 's|input("Please enter an email address: ")|"tkosciuch@luc.edu"|g' check_and_download_database.py

source /root/.profile
source /root/miniconda/etc/profile.d/conda.sh
