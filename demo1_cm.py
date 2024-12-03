## 4) Write a demo file, called "demo1_cm.py", that demonstrate
##    the use of the three functions of the package. The type of
##    demonstration is up to you, but it should be clear and 
##    informative. 
##    [10]

import cluster_maker as cm
import pandas as pd
import numpy as np



column_specs = {'A' : {'name': 'A', 'reps': [1, 2, 3, 4, 5]},
                'B': {'name': 'B', 'reps': [6, 7, 8, 9, 10]},
                'C': {'name': 'C', 'reps': [11, 12, 13, 14, 15]}}
#a list of dictionaries
# a list of dictionaries, which contain one key, whose value is a string
# and another key whose value is a list of integers
# I need a list, of which every element is a dictionary
seed_df = cm.define_dataframe_structure(column_specs)

dataframe = cm.simulate_data(seed_df, 100, column_specs)

cm.export_to_csv(dataframe, 'data.csv', delimiter=",", include_index=False)

