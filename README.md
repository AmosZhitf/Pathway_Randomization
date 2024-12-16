# Pathway Randomization

## Sparsity is All You Need: Rethinking Pathway-Informed Approaches in Deep Learning

### Overview
This repository provides tools and resources for pathway randomization in neural networks for omics data analysis. It includes a schematic representation of pathway integration approaches and their randomization, as shown below:

![Schematic Workflow](Figures/Workflow.jpg)

### Repository Structure
- **`Data/`**: Contains a dummy example matrix for use with the `Usage_Guide.ipynb` tutorial.
- **`Randomization_Function.py`**: Implements the `Pathway_Randomization` function to randomize connections while preserving defined constraints.
- **`Usage_Guide.ipynb`**: A tutorial notebook demonstrating how to use the `Pathway_Randomization` function.

---

## Function: `Pathway_Randomization`

The `Pathway_Randomization` function shuffles the positions of ones in a binary matrix while maintaining specified constraints, depending on the chosen mode. 
### Parameters:
- **`original_array (np.ndarray)`**:  
  The input binary matrix to shuffle.

- **`mode (str)`**:  
  Defines the shuffling constraints:
  - `'row'`: Maintains the number of ones in each row.
  - `'column'`: Maintains the number of ones in each column.
  - `'global'`: Preserves the total number of ones in the matrix.
  - `'sparsity'`: Adjusts the total number of ones to achieve a desired sparsity level.

- **`sparsity (float, optional)`**:  
  Specifies the desired sparsity level (applicable when `mode='sparsity'`).

- **`seed (int, optional)`**:  
  Random seed for reproducibility.

### Use Cases:
This function can be used to shuffle different types of matrices for the following modalities:

- **Pathway-Guided Network Topology (PGNT)**:  
  - **Gene-pathway connection matrices**: Ensures that the number of genes per pathway can be kept constant.  
  - **Pathway-pathway interaction matrices**

- **Pathway-Based Data Transformation (PBDT)**:  
  - **Adjacency matrices related to pathways**: Used to construct graphs for pathway representations.  
  - **Pathway images**: Supports the generation of images based on pathway data.

### Returns:
- **`np.ndarray`**:  
  A shuffled binary matrix with the desired constraints.

---

### Installation

Clone the repository and install dependencies:

1. Clone the repo

```git clone https://github.com/compbiomed-unito/Pathway_Randomization.git```
```cd Pathway_Randomization```


With Conda:

2. Create conda environment

```conda env create --name pathway_randomization_env --file=environment.yml```

3. Activate conda environment

```conda activate pathway_randomization_env```

With PIP:

2. Install requirements

```pip install -r requirements.txt```


## References

The following models and datasets were referenced during development. Links to their repositories are provided:

- **[PASNet](https://github.com/DataX-JieHao/PASNet)** (2018)
- **[CoxPASNet](https://github.com/DataX-JieHao/Cox-PASNet)** (2018)
- **[MiNet](https://github.com/DataX-JieHao/MiNet)** (2019)
- **[pathDNN](https://github.com/Charrick/drug_sensitivity_pred)** (2020)
- **[Multi-scale NN](https://life.bsc.es/iconbi/MultiScaleNN/index.html)** (2020)
- **[PathCNN](https://github.com/mskspi/PathCNN)** (2021)
- **[P-NET](https://github.com/marakeby/pnet_prostate_paper)** (2021)
- **[PathGNN](https://github.com/BioAI-kits/PathGNN)** (2022)
- **[MPVNN](https://github.com/gourabghoshroy/MPVNN)** (2022)
- **[BINN](https://github.com/InfectionMedicineProteomics/BINN)** (2023)
- **[PINNet](https://github.com/DMCB-GIST/PINNet)** (2023)
- **[DeepKEGG](https://github.com/lanbiolab/DeepKEGG)** (2024)
- **[GraphPath](https://github.com/amazingma/GraphPath)** (2024)
- **[Autosurv](https://github.com/jianglindong93/AUTOSurv)** (2024)
- **[Pathformer](https://github.com/lulab/Pathformer)** (2024)


