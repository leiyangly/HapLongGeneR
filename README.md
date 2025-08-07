# HapLongGeneR

**A modular pipeline for finding and annotating retrocopied genes in haploid long-read genome assemblies.**

> This software is in very early alpha.

## Overview

- HapLongGeneR discovers candidate retrocopied genes from haploid long-read assemblies.
- The package provides tools to annotate and summarise these retrocopies.
- Placeholder implementation: core functionality will be added in future updates.

## Installation

### Install using git and pip

Install dependencies (optional):
```bash
conda install -c bioconda minimap2 bedtools emboss blast repeatmasker
```

Clone the repository:
```bash
git clone https://github.com/leiyangly/HapLongGeneR.git
```

Install HapLongGeneR with pip:
```bash
cd HapLongGeneR

pip install -e .
```

### Install as a conda package (to be implemented)

Enable the required channels:
```bash
conda config --add channels defaults
conda config --add channels bioconda
conda config --add channels conda-forge
```

Install HapLongGeneR:
```bash
conda install haplonggener
```

## Usage

Run `haplonggener`, `haplonggener discover`, or `haplonggener annotate` with no arguments to see the available options.

### Discover mode: Identify retrocopied genes

Input:
- Haploid assembly FASTA

Output:
- Placeholder output describing discovered retrocopies

### Annotate mode: Annotate discovered retrocopies

Input:
- File containing candidate retrocopied genes

Output:
- Placeholder output with annotations

## Authors

Lei Yang, Sara Nematbakhsh, Amanda Norseen, and Rick McLaughlin
