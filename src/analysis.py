import pandas as pd

df = pd.read_csv('../data/dataset-spotify.csv')
pd.set_option('display.max_columns', None)

#column data types
data_types = df.dtypes

#return true if missing, false if not
empty_values = df.isnull()

#print(df.isnull().sum())

#One row has missing values in three columns
#print(df[df.isnull().any(axis=1)])
#print(df.loc[[0, 1]])

#All values of min and max where in the specified range according to the dataset documentation
description = df.describe()
#print(description)



