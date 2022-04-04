FROM ubuntu:focal

SHELL ["/bin/bash", "-c"]

# Update OS, install any needed packages here
RUN apt-get update && apt-get install -y autoconf \
    automake \
    gcc \
    git \
    libbz2-dev \
    liblzma-dev \
    libcurl4-gnutls-dev \
    libssl-dev \
    libncurses5-dev \
    make \
    ncbi-blast+ \
    perl \
    wget \
    zip \
    zlib1g-dev

COPY install2.sh /root

ENV PATH=/root/miniconda/bin/:/root/SPAdes-3.15.4-Linux/bin/:/root/bwa-0.7.17:$PATH

ENV PLATON_DB=/root/db/

RUN chmod 755 /root/install2.sh

RUN /root/install2.sh

#workaround for activating environments with a docker
RUN conda create -n recycler -y python=2.7
RUN conda run -n recycler conda install -c bioconda recycler

COPY download_db.sh /root

RUN chmod 755 /root/download_db.sh

RUN /root/download_db.sh

# this main.sh is the script for our program. As the path to main.sh is not specified, it assumes it's added to path
# ENTRYPOINT ["main.sh"]
