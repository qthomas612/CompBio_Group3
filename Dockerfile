#Dependencies: SPAdes, recycler, samtools, platon, & plasforest.

FROM ubuntu:focal

# Update OS, install any needed packages here
RUN  apt-get update \
  && apt-get install -y wget \
  && rm -rf /var/lib/apt/lists/
   # autoconf && \
   # apt-utils && \
   # gcc && \
   # libbz2-dev && \
   # liblzma-dev && \
   # libcurl4-gnutls-dev && \
   # libssl-dev && \
   # libncurses5-dev && \
   # make && \
   # ncbi-blast+ && \
   # perl && \
   # zlib1g-dev

# install conda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ./miniconda.sh
RUN bash ./miniconda.sh -b -p $HOME/miniconda
RUN export PATH="$HOME/miniconda/bin:$PATH"
#RUN conda activate base
#SHELL ["conda","run", "activate", "base"]

# spades 3.15.4 install
RUN wget https://cab.spbu.ru/files/release3.15.4/SPAdes-3.15.4-Linux.tar.gz && \
    tar -xzf SPAdes-3.15.4-Linux.tar.gz && \
    rm SPAdes-3.15.4-Linux.tar.gz
ENV PATH=$HOME/SPAdes-3.15.4-Linux/bin/:$PATH

# recycler install. recycler is built in python 2.7 so may cause not run properly in python 3. Gotta install conda for platon anyway so we could switch to a python 2.7 conda env when running recycler 
RUN wget https://github.com/Shamir-Lab/Recycler/releases/download/v0.7/Recycler-v0.7.zip && \
    unzip Recycler-v0.7.zip && \
    rm Recycler-v0.7.zip && \
    cd Recycler-0.7 && \
    python3 setup.py install --user && \
    cd ~/

# samtools install
RUN wget https://github.com/samtools/samtools/releases/download/1.15/samtools-1.15.tar.bz2 && \
    tar -xf samtools-1.15.tar.bz2 && \
    cd samtools-1.15 && \
    make && \
    make install && \
    cd ~/

# platon install
RUN conda install -c conda-forge -c bioconda -c defaults -y platon && \
    wget https://zenodo.org/record/4066768/files/db.tar.gz && \
    tar -xzf db.tar.gz && \
    rm db.tar.gz
ENV PLATON_DB=$HOME/db 

# plasforest install. downloading the database for plasforest may require a prompt, not sure how to run it silently at this time but hopefully it just works!
RUN git clone https://github.com/leaemiliepradier/PlasForest && \
    cd PlasForest && \
    tar -zxvf plasforest.sav.tar.gz && \
    chmod 755 database_downloader.sh && \
    ./database_downloader.sh
