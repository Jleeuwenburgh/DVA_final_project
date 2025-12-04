'''
Generates data profiles using ydata profiling.
For the datasets:
- heart disease
'''

import ydata_profiling as yp
import pandas as pd

folder = 'data/'
output_folder = 'profile_reports/'

datasets = ['heart.csv']

for dataset in datasets:
    df = pd.read_csv(folder + dataset)
    profile = yp.ProfileReport(df, title=f"{dataset.split('.')[0].capitalize()} Data Profile", explorative=True)
    profile.to_file(output_folder + f"{dataset.split('.')[0]}_data_profile.html")