# Empirical Study Based on OpenCollective

This repository contains the code and data for an empirical study examining open-source projects on the OpenCollective platform. The study analyzes various factors that influence the sustainability and funding of open-source projects, with a focus on the relationship between project activity and external sponsorship. The project is structured as follows:

## Folder Structure

### `data/`

Contains raw and processed data files used in the analysis, organized by research question (RQ).

* **`RQ1/`**
  
* **`RQ2/`**
  This folder contains processed data related to Research Question 2, which focuses on the factors that affect project funding on OpenCollective:

  * `data.csv`: A combined dataset for analysis.
  * `oc.csv`: Raw data related to OpenCollective funding.
  * `repo.csv`: Data about repositories associated with OpenCollective projects.
  * `RQ2_data.csv`: Additional processed data for RQ2 analysis.
  * `twitter_info.csv`: Data related to Twitter account information of the projects.
* **`RQ3/`**
  This folder contains data used for Research Question 3, which involves regression analysis to understand the impact of various factors on project donations and activity:

  * **`base_info.csv`** : This is the raw data file containing general information about the projects, which is used as the basis for creating other datasets.
  * **`commit_info.csv`, `issue_info.csv`, `spend_info.csv`** : These files are extracted from `base_info.csv` and contain detailed information about commits, issues, and project spend respectively.
  * **`commit.csv`, `issue.csv`** : These datasets are filtered from `commit_info.csv` and `issue_info.csv` based on specific criteria to isolate relevant entries for further analysis.
  * **`regression_data.csv`** : The final dataset used for regression analysis, combining relevant variables from the various files.
  * **`regression_data_base.csv`** : A version of the regression dataset with additional base information, used as a reference and a foundation for generating the final regression model dataset (`regression_data.csv`).

### `src/`

Contains source code for data collection, preprocessing, and analysis.

* **`data_collect/`**
  Contains scripts for collecting data from various sources, primarily utilizing the GitHub REST API and the Open Collective Public GraphQL API to gather information related to open-source projects, including repository details, commits, issues, and sponsorship data.:
  * `add-dates.py`: Script to add date information to data.
  * `check-repo.py`: Script to check repository data.
  * `extract.py`: General data extraction script.
  * `grab-all-repo.py`: Script to gather all repository data.
  * `grab-commit.py`: Script to collect commit data.
  * `grab-detail.py`: Collects detailed project information.
  * `grab-issue.py`: Script for gathering issue data.
  * `grab-oc.py`: Collects OpenCollective-related data.
  * `statis.py`: Performs statistical analysis on the collected data.
* **`RQ2/`**
  Contains scripts for preprocessing and merging data for Research Question 2:
  * `data_preprocess.py`: Preprocesses data for RQ2 analysis.
  * `filter_twitter.py`: Filters and processes Twitter-related data for projects.
  * `merge_data.py`: Merges various datasets for RQ2 analysis.
* **`RQ3/`**
  Contains scripts for preprocessing and analysis related to Research Question 3:
  * `data_preprocess.py`: Prepares data for RQ3 analysis.
  * `generate_graph.ipynb`: Jupyter notebook for generating graphs related to RQ3.
  * `mergeSponsor.py`: Merges sponsor-related data for analysis.
  * `modifyDataForAnalysis.py`: Prepares the data for regression analysis in RQ3.
