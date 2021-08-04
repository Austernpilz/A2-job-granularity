# Metagenome read mapping approaches

This repository contains multiple examples of scientific workflows. The goal of this repository is to write workflow components for mapping metagenomics reads that can be used on different architectures. 

The repository is divided into subprojects, details of each below.

## Running

To run the snakemake workflow in one of the subfolders:
`snakemake --use-conda --cores {e.g 8}`

Other useful flags:
1. `--force-use-threads` force threads instead of processes in case each process takes too much local memory to be run in parallel 
2. `--dag` don't run any jobs just create a figure of the directed acyclic graph
3. `--dryrun` don't run any jobs just display the order in which they would be executed.

## raptor_data_simulation
Simulating DNA sequences with https://github.com/eseiler/raptor_data_simulation.
Run this workflow before running either MG-1 or MG-2. The data simulation parameters are set in `simulation_config.yaml`. Both MG-1 and MG-2 have a separate configuration file called `search_config.yaml` where prefiltering and search parameters should be set. 

## MG-1

This workflow is optimized to be run on a local system with large main memory and multiple threads. The large main memory is used when working with the IBF (at least 1GB) which has to be read completely into memory. The FM-indices, IBF creation and read mapping are done using 8 threads. 


Steps of workflow:
1. Simulate data with the raptor data simulation:
2. Create an IBF over the simulated reference data
3. Create an FM-index for each of the bins of the reference
4. Map each read to the FM-index determined by IBF pre-filtering

---

**NOTE:** Raptor data simulation and DREAM-Yara are not available through conda and have to be built from source. Also add location of DREAM-Yara binaries to $PATH.

Data simulation repo:
https://github.com/eseiler/raptor_data_simulation

DREAM-Yara repo:
https://github.com/temehi/dream_yara

---

## MG-2

This version of a metagenomics workflow aims to work around the constraint of having low memory. A hash table based approach is used instead of the IBF.

Steps of workflow:
1. Simulate data with the raptor data simulation:
2. Create a hash table over the simulated reference data
3. Create an FM-index for each of the bins of the reference
4. Map each read to the FM-index determined by hashmap pre-filtering

### HashMap

https://github.com/eaasna/low-memory-prefilter

Create a hash table where the keys are the complete set of k-mers. The value corresponding to a key is a list of all the bins that contain this k-mer.  

# Outdated

## MG-R 
This is a state of the art representative workflow for mapping metagenomic reads. NB! Needs an update.

---

taxSBP repo:
https://github.com/pirovc/taxsbp

---

**NOTE:** taxSBP requires additional inputs (merged.dmp and nodes.dmp) which are currently not downloaded as part of the workflow. There is also a `seqinfo.tsv` file that has to be created specifically for each reference dataset. See tacSBP repo for more details. It might additionally be necessary to remove - and / characters from the reference file (.fasta sequence IDs).

## alternative_tools

This subprojects has currently been abandoned and might be broken. These are tools that did not fit into the representative workflow but are nevertheless state of the art and widely used.

STELLAR documentation:
https://github.com/seqan/seqan/tree/master/apps/stellar

Raptor documentation:
https://github.com/seqan/raptor

Yara read mapper:
https://github.com/seqan/seqan/blob/develop/apps/yara/README.rst
