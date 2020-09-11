# exVariance

**A tool for integrated analysis the liquid biopsy sequencing data**

<!-- **Tutorial:** [https://shangzhang.github.io/exVariance/](https://shangzhang.github.io/exVariance/) -->

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
  - [Best Practice](#best-practice)
  - [Docker image](#docker-image)
  - [Singularity image](#singularity-image)
- [Download References](#download-references)
- [Usage](#usage)
  - [Help message](#help-message)
  - [Input files](#input-files)
  - [Run](#run)
- [System Requirements](#system-requirements)
- [Copyright and License Information](#copyright-and-license-information)
- [Citation](#citation)

---

## Installation

### Best Practice
Install the [github](https://github.com/ShangZhang/exVariance) source code and ependencies below listed:

  ```bash
    git clone https://github.com/ShangZhang/exVariance.git
  ```

#### Dependencies:
  1. [Anaconda3](https://www.anaconda.com)/[Miniconda3](http://conda.pydata.org/miniconda.html) conda version latter than 4.8.4
  2. [Python](https://www.python.org/) version latter than 3.8.3
  3. [Snakemake](https://snakemake.readthedocs.io) version=5.14.0
  4. [R](https://www.r-project.org/) version=3.6.3
  5. [R packages](https://www.r-project.org/)
      
#### How to install all the dependencies:
1. Install **Anaconda3/Minicodna3** and **Python**
    ```
    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
    bash Miniconda3-latest-Linux-x86_64.sh
    ```
    - Whilst running the installation script, follow the commands listed on screen, and press the enter key to scroll.
    - Make sure to answer yes when asked if you want to prepend Miniconda3 to PATH.
    - Close your terminal, open a new one and you should now have Conda working! Test by entering:
      ```
      conda update conda
      ```
      - Press y to confirm the conda updates
2. Install **Mamba**
  The default conda solver is a bit slow and sometimes has issues with selecting the special version packages. Therefore, we recommend to install Mamba as a drop-in replacement via
    ```bash
    conda install -c conda-forge mamba
    ```
3. Install **Snakemake 5.14.0** and **R 3.6.3**
    ```
    mamba create -n exvariance4 -c conda-forge -c bioconda snakemake=5.14.0 r-base=3.6.3 -y
    ```
4. Install related **R packages**
    **Best Practice**
    ```r
    mamba install -c r -c conda-forge -c bioconda -c eugene_t r-argparse r-clustersim r-ggpubr bioconductor-scater bioconductor-scran bioconductor-singlecellexperiment bioconductor-sva bioconductor-edger bioconductor-ruvseq r-kbet r-devtools -y
    ```
    ```r
    devtools::install_github(c("hemberg-lab/scRNA.seq.funcs","theislab/kBET"))
    ```
    **OR**
    ```R
    install.packages(c("argparse","clusterSim","ggpubr","BiocManager","devtools"))
    BiocManager::install(c("scater","scran","SingleCellExperiment","sva","edgeR","RUVSeq"))
    devtools::install_github(c("hemberg-lab/scRNA.seq.funcs"))
    devtools::install_github(c("theislab/kBET"))
    ```
    
### Docker image
For easy installation, you can use the [exVariance image](https://hub.docker.com/) of [docker](https://www.docker.com) with all dependencies installed:

  ```bash
    docker pull <exVariance_image>
  ```

  - dependencies
    1. [docker](https://www.docker.com/) version>=19.03.4

### Singularity image
Alternatively, you can use use [singularity](https://singularity.lbl.gov/) or [udocker](https://github.com/indigo-dc/udocker) to run the container for Linux kernel < 3 or if you don't have permission to use docker.


## Download References
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

                  { RNA_seq_pre_process,RNA_seq_exp_matrix,
                    RNA_seq_fusion_transcripts,RNA_seq_RNA_editing,
                    RNA_seq_SNP,RNA_seq_APA,RNA_seq_AS,
                    DNA_seq_ctDNA_mutation,DNA_seq_NP,
                    DNA_meth_WGBS,DNA_meth_RRBS,
                    DNA_meth_Seal_seq,DNA_meth_Methyl-cap_seq,
                    DNA_meth_MeDIP_seq,DNA_meth_MCTA_seq
                    }

exVariance is a tool for integrated analysis the liquid biopsy sequencing data.

positional arguments:
  { RNA_seq_pre_process,RNA_seq_exp_matrix,
    RNA_seq_fusion_transcripts,RNA_seq_RNA_editing,
    RNA_seq_SNP,RNA_seq_APA,RNA_seq_AS,
    DNA_seq_ctDNA_mutation,DNA_seq_NP,
    DNA_meth_WGBS,DNA_meth_RRBS,
    DNA_meth_Seal_seq,DNA_meth_Methyl-cap_seq,
    DNA_meth_MeDIP_seq,DNA_meth_MCTA_seq
    }

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
  { RNA_seq_pre_process,RNA_seq_exp_matrix,
    RNA_seq_fusion_transcripts,RNA_seq_RNA_editing,
    RNA_seq_SNP,RNA_seq_APA,RNA_seq_AS,
    DNA_seq_ctDNA_mutation,DNA_seq_NP,
    DNA_meth_WGBS,DNA_meth_RRBS,
    DNA_meth_Seal_seq,DNA_meth_Methyl-cap_seq,
    DNA_meth_MeDIP_seq,DNA_meth_MCTA_seq
    }

For additional help or support, please visit https://github.com/ShangZhang/exVariance

```

### Input files

RNA-seq related examples can be found in `demo` directory with the following structure:

```text
    ./demo/*/
    |-- config
    |   |-- default_config.yaml
    |   |-- <data_name>.yaml
    |   |-- dapars_configure.txt
    |   `-- RNAEditor_configure.txt
    |-- data
    |   |-- fastq/
    |   |-- sample_ids.txt
    |   |-- sample_classes.txt
    |   |-- compare_groups.yaml
    |   `-- batch_info.txt
    |-- output
    `-- summary
```

Other related examples can be found in `demo` directory with the following structure:

```text
    ./demo/*/
    |-- config
    |   |-- default_config.yaml
    |   `-- <data_name>.yaml
    |-- data
    |   |-- fastq/
    |   `-- sample_ids.txt
    |-- output
    `-- summary
```

> **Note:**
>
> - `config/default_config.yaml`: the default configuration file. If you don't understand, don't change the content.
> - `config/<data_name>.yaml`: the user defined configuration file, to point out the related used path.
> - `data/fastq/` : directory contain samples name, suffixed with 'fastq' 'fasta.gz' or 'fastq.gz'.
> - `data/sample_ids.txt`: table of sample names (remove the suffix 'fastq' 'fasta.gz' or 'fastq.gz' )
> - `output/`: the output directory
> - `summary/` : contain the summary files

You can create your own data directory with the above directory structure.
Multiple datasets can be put in the same directory by replacing "example" with your own dataset names.

### Run

![exVariance analysis](docs/imgs/ExVariance_analysis.svg)

#### For RNA-seq realted analysis
```bash
exVariance -u <USER_CONFIG_FILE> RNA_seq_pre_process
```
```bash
exVariance -u <USER_CONFIG_FILE> RNA_seq_exp_matrix

exVariance -u <USER_CONFIG_FILE> RNA_seq_fusion_transcripts

exVariance -u <USER_CONFIG_FILE> RNA_seq_RNA_editing

exVariance -u <USER_CONFIG_FILE> RNA_seq_SNP

exVariance -u <USER_CONFIG_FILE> RNA_seq_APA

exVariance -u <USER_CONFIG_FILE> RNA_seq_AS
```

#### For DNA-methylation realted analysis
```bash
exVariance -u <USER_CONFIG_FILE> DNA_meth_WGBS

exVariance -u <USER_CONFIG_FILE> DNA_meth_RRBS

exVariance -u <USER_CONFIG_FILE> DNA_meth_Seal_seq

exVariance -u <USER_CONFIG_FILE> DNA_meth_Methyl-cap_seq

exVariance -u <USER_CONFIG_FILE> DNA_meth_MeDIP_seq

exVariance -u <USER_CONFIG_FILE> DNA_meth_MCTA_seq
```

#### For DNA-seq realted analysis
```bash
exVariance -u <USER_CONFIG_FILE> DNA_seq_ctDNA_mutation

exVariance -u <USER_CONFIG_FILE> DNA_seq_NP
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
