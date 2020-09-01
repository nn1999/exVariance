**Tutorial:** [https://shangzhang.github.io/exVariance/](https://shangzhang.github.io/exVariance/)

---

<p align="left">
<a href="https://github.com/ShangZhang/exVariance">
    <img alt="exVariance GitHub Pipenv locked Python version" src="https://img.shields.io/github/pipenv/locked/python-version/ShangZhang/exVariance?style=flat"></a>
<a href="https://github.com/ShangZhang/exVariance">
    <img alt="exVariance Docker Build Status" src="https://img.shields.io/docker/build/ShangZhang/exVariance?style=flat"></a>
<a href="https://github.com/ShangZhang/exVariance">
    <img alt="exVariance GitHub release (latest by date)" src="https://img.shields.io/github/v/release/ShangZhang/exVariance?style=flat"></a>
<a href="https://github.com/ShangZhang/exVariance">
    <img alt="exVariance GitHub forks" src="https://img.shields.io/github/forks/ShangZhang/exVariance?style=flat"></a>
<a href="https://github.com/ShangZhang/exVariance">
    <img alt="exVariance GitHub stars" src="https://img.shields.io/github/stars/ShangZhang/exVariance?style=flat"></a>
</p>

---

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

- For easy installation, you can use the [exVariance image](https://hub.docker.com/) of [docker](https://www.docker.com) with all dependencies installed:

  ```bash
    docker pull <exVariance_image>
  ```

- Alternatively, you can use use [singularity](https://singularity.lbl.gov/) or [udocker](https://github.com/indigo-dc/udocker) to run the container for Linux kernel < 3 or if you don't have permission to use docker.

- Also, you can also use the [github](https://github.com/ShangZhang/exVariance) source code and install dependencies below listed:

  ```bash
    git clone https://github.com/ShangZhang/exVariance.git
  ```

  - dependencies:
    1. [anaconda](https://www.anaconda.com) version=4.8.4
    2. [python] version=3.7
    2. [snakemake](https://snakemake.readthedocs.io) version=5.4.0
    3. [docker](https://www.docker.com/) version=19.03.4
    
    - how to install special vesion of python and snakemake
      1. install the Miniconda/Anaconda Python3 distribution
      2. The default conda solver is a bit slow and sometimes has issues with selecting the latest package releases. Therefore, we recommend to install Mamba as a drop-in replacement via
        ```bash
          conda install -c conda-forge mamba
        ```
      3. you can install Snakemake with
        ```bash
          mamba create -n exvariance -c conda-forge -c bioconda python=3.7 snakemake=5.4.0 -y
        ```

## Usage

### Help message

Run `exVariance --help` to get the usage:

```text
usage: ./bin/exVariance [-h] --user_config_file USER_CONFIG_FILE

              [--cluster]
              [--cluster-config CLUSTER_CONFIG]
              [--cluster-command CLUSTER_COMMAND]
              [--singularity SINGULARITY]
              [--singularity-wrapper-dir SINGULARITY_WRAPPER_DIR]

              {quality_control,cutadapt,quality_control_clean,mapping,bigwig,count_matrix,normalization,
              differential_expression,fusion_transcripts,SNP,RNA_editing,AS,APA,WGBS,RRBS,ctdna}

exVariance is a Integrated Analysis Tool for Liquid Biopsy Sequencing Data.

optional arguments:
  -h, --help            show this help message and exit
  --user_config_file USER_CONFIG_FILE, -u USER_CONFIG_FILE
                        the user config file.
                        (<data_name>/config/<data_name>.yaml
                        for example)

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
  {quality_control,cutadapt,quality_control_clean,mapping,bigwig,count_matrix,normalization,
  differential_expression,fusion_transcripts,SNP,RNA_editing,AS,APA,WGBS,RRBS,ctdna}
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

## Copyright and License Information

Copyright (C) Lu Lab @ Tsinghua University, Beijing, China 2020 All rights reserved

## Citation