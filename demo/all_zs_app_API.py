# RNA types for sequential mapping in small-RNA pipeline
rna_types: [univec, rRNA, lncRNA, miRNA, mRNA, piRNA, snoRNA, 
  snRNA, srpRNA, tRNA, tucpRNA, Y_RNA]
# Adjusted p-value threshold for defining domains
call_domain_pvalue: "05"
# Distribution to use to model read coverage in each bin
distribution: ZeroTruncatedNegativeBinomial
# Size of each bin to compute read coverage
bin_size: 20
# Define recurrent domain as domains called in fraction of samples above this value
cov_threshold: 0.05
# Method to scale features
scale_method: robust
# Classifier for feature selection
classifiers: random_forest
# Number of features to select
#n_selects: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n_selects: [10]
resample_method: bootstrap
# Feature selection methods
#select_methods: [robust]
# Enable zero fraction filter
zero_fraction_filter: false
# Parameters for zero fraction filter
zero_fraction_filter_params:
  threshold: 0.8
# Enable log transformation
log_transform: true
# Parameters for log transformation
log_transform_params:
  base: 2
  pseudo_count: 1
# Enable RPM filter
rpm_filter: false
# Parameters for RPM filter
rpm_filter_params:
  threshold: 10
# Fold change filter
fold_change_filter: false
# Parameters for fold change filter
fold_change_filter_params:
  direction: any
fold_change_filter_direction: [any]
# Feature scaling method
scaler: zscore
# Parameters for feature scaling
scaler_params:
  zscore:
    with_mean: true
  robust:
    with_centering: true
# Enable differential expression filter
diffexp_filter: false
# Parameters for differential expression filter
diffexp_filter_params:
  method: [deseq2]
  score_type: pi_value
  fold_change_direction: any
# Wrapper feature selection method
#selector: robust
selector: [max_features, robust]
# Parameters for wrapper feature selection method
selector_params:
  robust:
    cv:
      splitter: stratified_shuffle_split
      n_splits: 10
      test_size: 0.1
  rfe:
    step: 0.2
  max_features: {}
    
# Maximum number of features to select
n_features_to_select: [10]
# Classifier for prediction
classifier: [logistic_regression, random_forest]
# Parameters for classifiers
classifier_params:
  logistic_regression:
    penalty: l2
    solver: liblinear
  logistic_regression_l1:
    penalty: l1
    solver: liblinear
  logistic_regression_l2:
    penalty: l2
    solver: liblinear
  random_forest:
    n_estimators: 50
    max_features: sqrt
  linear_svm:
    dual: True
# Parameters for cross-validation
cv_params:
  splitter: stratified_shuffle_split
  n_splits: 50
  test_size: 0.1
# Method for computing sample-weight
sample_weight: auto

# Enable grid search for optimizing hyper-parameters in classifiers
grid_search: true
# Parameters for grid search for classifier parameters
grid_search_params:
  param_grid:
    logistic_regression:
      C: [0.00001, 0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000, 100000]
    logistic_regression_l1:
      C: [0.00001, 0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000, 100000]
    logistic_regression_l2:
      C: [0.00001, 0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000, 100000]
    linear_svm:
      C: [0.00001, 0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000, 100000]
    random_forest:
      n_estimators: [25, 50, 75]
      max_depth: [3, 4, 5]
    decision_tree:
      max_depth: [2, 3, 4, 5, 6, 7, 8]
  cv:
    splitter: stratified_kfold
    n_splits: 5
  iid: false
  scoring: roc_auc
# Parameters for evalation of features
evaluation_features:
  classifier: logistic_regression
  classifier_params:
    logistic_regression:
      penalty: l2

# Splitter for cross-validation
cv_splitter: stratified_shuffle_split
# Number of cross-validation folds for grid search
grid_search_n_splits: 5
# Number of train-test splits for cross-validation
cv_n_splits: 50
# Fraction/number of test samples in cross-validation
cv_test_size: 0.2
# Compute sample weight for imbalanced classes
compute_sample_weight: true
# Fold change filter in feature selection (up, down, both)
fold_change_direction: up
# Fold change filter threshold
fold_change_threshold: 1
# Fraction of features to eliminate in each RFE step
rfe_step: 0.1
# Number of cross-validation splits in RFE
rfe_n_splits: 10
# Number of cross-validation splits in robust feature selection
robust_feature_selection_n_splits: 10
# Splitter for robust feature selection
robust_feature_selection_splitter: stratified_shuffle_split

# Number of random train-test splits for cross-validation
cross_validation_splits: 50
# Type of counts for feature selection
#   domains_combined: combine miRNA/piRNA with long RNA domains
#   transcript: transcript-level features
#   featurecounts: gene-level features counted using featureCounts
count_method: domains_combined
# Define low expression value as read counts below this value
filtercount: 5
# Threshold for filtering low expression features
filterexpv: 0
# Quantification method for low expression filter
filtermethod: filtercount
# Keep features with high expression in fraction of samples above this value
filtersample: 0.2
# Imputation methods to try (set to "null" to skip imputation)
#imputation_methods: ["viper_count", "null"]
imputation_method: ["null"]
# Read depth normalization methods to try
normalization_method: ["TMM"]
# Batch effect removal methods to try (set "null" to skip batch effect removal)
batch_removal_method: ["ComBat"]
# Column index of batch effect in batch_info.txt to considier for Combat
batch_index: 1
    
# Root directory
root_dir: "."
# Directory for sequences and annotations
genome_dir: "genome/hg38"
# Temporary directory (e.g. samtools sort, sort)
temp_dir: "tmp"
# Directory for third-party tools
tools_dir: "tools"
# Directory for exSeek scripts
bin_dir: "bin"
# Directory for spike-in sequences and index
spikein_dir: "genome/hg38/spikein"

# Input files are clean reads
input_clean_reads: false

# Number of threads for uncompression and compression
threads_compress: 1
# Default number of threads to use
threads: 1
# alignment software to use (valie choices: bowtie, star)
aligner: bowtie2
# Remove 3'-end adaptor sequence from single-end reads
adaptor: ""
# Remove 5'-end adaptor sequence from single-end reads
adaptor_5p: ""
# Remove 3'-end adaptor sequence from the first read in a pair
adaptor1: ""
# Remove 3'-end adaptor sequence from the second read in a pair
adaptor2: ""
# Remove 5'-end adaptor sequence from the first read in a pair
adaptor1_5p: ""
# Remove 5'-end adaptor sequence from the second in a pair
adaptor2_5p: ""
# Exact number of bases to trim from 5'-end
trim_5p: 0
# Exact number of bases to trim from 3'-end
trim_3p: 0
# Trim exact number of bases after adapter trimming
trim_after_adapter: false
# Discard reads of length below this value
min_read_length: 16
# Maximum read length
max_read_length: 100
# Trim bases with quality below this value from 3'-end
min_base_quality: 30
# Trim bases with quality below this value from 5'-end
min_base_quality_5p: 30
# Trim bases with quality below this value from 3'-end
min_base_quality_3p: 30
# Quality encoding in FASTQ files
quality_base: 33
# Strandness (valid choices: forward, reverse, no)
strandness: forward
# Filter out reads with mapping quality below this value
min_mapping_quality: 0
# Only considier longest transcript for transcriptome mapping
use_longest_transcript: true
# Expected read length for mapping using STAR
star_sjdboverhang: 100
# Number of threads for mapping
threads_mapping: 4
# Remove duplicates for long RNA-seq before feature counting
remove_duplicates_long: true
# Input reads are paired-end
paired_end: false
# Use small RNA-seq pipeline (sequential mapping)
small_rna: true
# Remove UMI tags (leading nucleotides)
umi_tags: false
# Length of the UMI barcode
umi_length: 0
# Evaluate published biomarkers
evaluate_features_preprocess_methods: []
# Differential expression method
# Available methods: deseq2, edger_glmlrt, edger_glmqlf, edger_exact, wilcox
diffexp_method: [deseq2, edger_glmlrt]
# Count multi-mapping reads
count_multimap_reads: true
# Count overlapping features
count_overlapping_features: true

# Base URL for IGV web server
igv_base_url: http://172.22.220.21:5000

# Configuration for singularity
singularity:
  image: singularity/exseek.simg
  wrapper_dir: singularity/wrappers

# Configuration for cluster jobs
cluster:
  # Command template for submitting a job to cluster
  submit_command: 'bsub -q {cluster.queue} -J {cluster.name} -e {cluster.stderr} -o {cluster.stdout} -R {cluster.resources} -n {cluster.threads}'
  # Snakemake configuration file for cluster jobs
  config_file: config/cluster.yaml



# default config
default_config_file: /home/zhangshang/work/app/app_dev/config/default_config.yaml

# file paths
root_dir: /home/zhangshang/work/app/app_dev

genome_dir: /home/zhangshang/ref/hg38
output_dir: /home/zhangshang/work/app/app_dev/output/long_pe_example
temp_dir: /home/zhangshang/work/app/app_dev/tmp
data_dir: /home/zhangshang/work/app/app_dev/data/long_pe_example

# general parameters
threads_compress: 2
threads_mapping: 4

# mapping parameters
aligner: STAR
adaptor1: AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC
adaptor2: AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT
paired_end: true
small_rna: false
strandness: forward
count_method: featurecounts
