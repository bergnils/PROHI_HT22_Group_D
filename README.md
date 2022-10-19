# PROHI_HT22_Group_D
## Getting started
### EDA
For a simple exploratory data analysis and some guidelines on basic importing and preprocessing of the datasets, go to `src/notebooks/heart_disease_dataset_EDA.ipynb`.
### Training the final model
In order to train and save a trained model as a pickle  file, run the notebook `src/notebooks/final_model_implementation.ipynb`. The pickled model will be saved in the `src/dash` folder.
### Dash application
A runnable dash application can be found at `src/dash/dash_file.py`. Note that the trained model mentioned above must be saved as a pickle file first.
## The datasets
This repository uses the four datasets found at http://archive.ics.uci.edu/ml/datasets/Heart+Disease, which can be found in the `data` folder in this repository.
