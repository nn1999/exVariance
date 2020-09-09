# exVariance

**A tool for integrated analysis the liquid biopsy sequencing data**

**Tutorial:** [https://shangzhang.github.io/exVariance/](https://shangzhang.github.io/exVariance/)

---

<p align="left">
<!-- <a href="https://github.com/ShangZhang/exVariance">
    <img alt="exVariance GitHub Pipenv locked Python version" src="https://img.shields.io/github/pipenv/locked/python-version/ShangZhang/exVariance?style=flat"></a>
<a href="https://github.com/ShangZhang/exVariance">
    <img alt="exVariance Docker Build Status" src="https://img.shields.io/docker/build/ShangZhang/exVariance?style=flat"></a>
<a href="https://github.com/ShangZhang/exVariance">
    <img alt="exVariance GitHub release (latest by date)" src="https://img.shields.io/github/v/release/ShangZhang/exVariance?style=flat"></a> -->
<a href="https://github.com/ShangZhang/exVariance">
    <img alt="exVariance GitHub forks" src="https://img.shields.io/github/forks/ShangZhang/exVariance?style=flat"></a>
<a href="https://github.com/ShangZhang/exVariance">
    <img alt="exVariance GitHub stars" src="https://img.shields.io/github/stars/ShangZhang/exVariance?style=flat"></a>
</p>


## Table of Contents:

- [Installation](#installation)
- [Usage](#usage)
  - [Help message](#help-message)
  - [Input files](#input-files)
  - [Run](#run)
- [Copyright and License Information](#copyright-and-license-information)
- [Citation](#citation)

---

## Installation

#### Docker image
For easy installation, you can use the [exVariance image](https://hub.docker.com/) of [docker](https://www.docker.com) with all dependencies installed:

  ```bash
    docker pull <exVariance_image>
  ```

  - dependencies
    1. [docker](https://www.docker.com/) version>=19.03.4

#### Singularity image
Alternatively, you can use use [singularity](https://singularity.lbl.gov/) or [udocker](https://github.com/indigo-dc/udocker) to run the container for Linux kernel < 3 or if you don't have permission to use docker.

#### Homemade
**Best Practice**: Also, you can also use the [github](https://github.com/ShangZhang/exVariance) source code and install dependencies below listed:

  ```bash
    git clone https://github.com/ShangZhang/exVariance.git
  ```

  - dependencies:
    1. [Anaconda3](https://www.anaconda.com)/[Miniconda3](http://conda.pydata.org/miniconda.html) conda version=4.8.4
    2. [Python](https://www.python.org/) version=3.7.9
    3. [Snakemake](https://snakemake.readthedocs.io) version=5.23.0
    
   
  > **Note:**
  > - how to install special vesion of snakemake？
      1. The default conda solver is a bit slow and sometimes has issues with selecting the latest package releases. Therefore, we recommend to install Mamba as a drop-in replacement via
        ```
            conda install -c conda-forge mamba
        ```
      2. you can install Snakemake with
        ```
            mamba create -n exVariance -c conda-forge -c bioconda python=3.7 snakemake=5.23.0 -y
        ```      
      
## Download Reference
exVariance is dependent on reference files which can be found for the supported species listed below: <u>hg38</u>

To unzip these files: tar -xzf hg19.tar.gz OR tar -xzf mm9.tar.gz

## Usage

### Help message

Run `exVariance --help` to get the usage:

```text
usage: exVariance [-h] --user_config_file USER_CONFIG_FILE

                  [--cluster]
                  [--cluster-config CLUSTER_CONFIG]
                  [--cluster-command CLUSTER_COMMAND]
                  [--singularity SINGULARITY]
                  [--singularity-wrapper-dir SINGULARITY_WRAPPER_DIR]

                  {quality_control,cutadapt,quality_control_clean,mapping,bigwig,
                   count_matrix,normalization,differential_expression,fusion_transcripts,
                   SNP,RNA_editing,AS,APA,WGBS,RRBS,ctdna,wgbs_rrbs,seal_methyl-cap_medip,
                   mcta,dna-seq}

exVariance is a tool for integrated analysis the liquid biopsy sequencing data.

positional arguments:
  {quality_control,cutadapt,quality_control_clean,mapping,bigwig,count_matrix,
   normalization,differential_expression,fusion_transcripts,SNP,RNA_editing,AS,APA,
   WGBS,RRBS,ctdna,wgbs_rrbs,seal_methyl-cap_medip,mcta,dna-seq}

optional arguments:
  -h, --help            show this help message and exit
  --user_config_file USER_CONFIG_FILE, -u USER_CONFIG_FILE
                        the user config file

  --cluster             submit to cluster
  --cluster-config CLUSTER_CONFIG
                        cluster configuration file

  --cluster-command CLUSTER_COMMAND
                        command for submitting job to cluster (default read
                        from {config_dir}/cluster_command.txt
  --singularity SINGULARITY
                        singularity image file
  --singularity-wrapper-dir SINGULARITY_WRAPPER_DIR
                        directory for singularity wrappers


positional arguments:
  {quality_control,cutadapt,quality_control_clean,mapping,bigwig,count_matrix,normalization,differential_expression,fusion_transcripts,SNP,RNA_editing,AS,APA,WGBS,RRBS,ctdna,wgbs_rrbs,seal_methyl-cap_medip,mcta,dna-seq}

For additional help or support, please visit https://github.com/ShangZhang/exVariance

```

### Input files

Several examples can be found in `demo` directory with the following structure:

```text
    ./demo/*/
    |-- config
    |   |-- default_config.yaml
    |   `-- example.yaml
    |-- data
    |   |-- fastq
    |   `-- sample_ids.txt
    |-- genome
    |   `-- fasta
    |-- output
    `-- tmp
```

> **Note:**
>
> - `config/default_config.yaml`: the default configuration file. If you don't understand, don't change the content.
> - `config/<data_name>.yaml`: the user defined configuration file, to point out the related used path.
> - `data/fastq/` : directory contain samples name, suffixed with 'fasta.gz' or 'fastq.gz'.
> - `data/example/sample_ids.txt`: table of sample names (remove the suffix 'fasta.gz' or 'fastq.gz' )
> - `genome/f` : the genome directory
> - `output/`: the output directory
> - `tmp/` : contain the temporary files

You can create your own data directory with the above directory structure.
Multiple datasets can be put in the same directory by replacing "example" with your own dataset names.

### Run

#### for paired_end/single_read whole genome bisulfite sequencing (WGBS) data

```bash
exVariance -u <USER_CONFIG_FILE> WGBS
```

#### for MspI_ApeKI_double_enzyme/normal reduced represented bisulfite sequencing (RRBS) data

```bash
exVariance -u <USER_CONFIG_FILE> RRBS
```

#### for ctDNA sequencing data

```bash
exVariance -u <USER_CONFIG_FILE> ctdna
```

#### for cell_free/exosome long/small paired_end/single_read RNA sequencing data

##### Pre-analysis

```bash
exVariance -u <USER_CONFIG_FILE> quality_control
exVariance -u <USER_CONFIG_FILE> cutadapt
exVariance -u <USER_CONFIG_FILE> quality_control_clean
exVariance -u <USER_CONFIG_FILE> mapping
exVariance -u <USER_CONFIG_FILE> bigwig
exVariance -u <USER_CONFIG_FILE> count_matrix
exVariance -u <USER_CONFIG_FILE> normalization
```

##### Analysis

```bash
exVariance -u <USER_CONFIG_FILE> differential_expression
exVariance -u <USER_CONFIG_FILE> fusion_transcripts
exVariance -u <USER_CONFIG_FILE> SNP
exVariance -u <USER_CONFIG_FILE> RNA_editing    ## for RNA editing analysis, the sequencing reads must more than 4000000 Sxequences.
exVariance -u <USER_CONFIG_FILE> AS
exVariance -u <USER_CONFIG_FILE> APA
```

## System Requirements:

Some of the tools that exVariance uses, e.g. STAR is very memory intensive programs.  Therefore we recommend the following system requirements for exVariance:

#### Minimal system requirements:
We recommend that you run exVariance on a server that has at least 48GB of ram.  This will allow for a single-threaded exVariance run (on human samples).

#### Recommended system requirements:
We recommend that you have at least 64GB of ram and at least a 4-core CPU if you want to run exVariance in multi-threaded mode (which will speedup the workflow significantly).  

Our own servers have 64GB of ram and 16 cores.

## Copyright and License Information

Copyright (C) Lu Lab @ Tsinghua University, Beijing, China 2020 All rights reserved

## Citation