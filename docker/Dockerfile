FROM ubuntu:bionic

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

ENV PATH=/root/Recycler-0.7/build/lib/:/root/miniconda/bin/:/root/Recycler-0.7/bin/:/root/samtools-1.15/:/root/PlasForest:/root/SPAdes-3.15.4-Linux/bin/:/root/bwa-0.7.17/:$PATH

ENV PLATON_DB=/root/db/

RUN chmod 755 /root/install.sh

RUN /root/install.sh

COPY download_db.sh /root

RUN chmod 755 /root/download_db.sh

COPY main.sh /usr/local/bin

RUN chmod 755 /usr/local/bin/main.sh

RUN /root/download_db.sh

COPY compile_results.py /root/compile_results.py

RUN chmod 755 /root/compile_results.py

# this main.sh is the script for our program. As the path to main.sh is not specified, it assumes it's added to path
#ENTRYPOINT ["main.sh"]
