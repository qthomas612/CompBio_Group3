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

COPY install.sh /root

ENV PATH=/root/miniconda/bin/:/root/SPAdes-3.15.4-Linux/bin/:$PATH

ENV PLATON_DB=/root/db/

RUN chmod 755 /root/install.sh

RUN /root/install.sh
