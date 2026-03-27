import pandas as pd

df = pd.read_csv('../data/dataset-spotify.csv')
pd.set_option('display.max_columns', None)

#row 65900 had three nan values and was deleted with dropna()
#print(df[df.isnull().any(axis=1)])
df = df.dropna()
#print(df[df.isnull().any(axis=1)])


#deleting unnecessary columns: unnamed, explicit, key, mode, time_signature,
df = df.drop(['explicit', 'key', 'mode', 'time_signature'], axis=1)
#print(df)

duplicates = df.duplicated()
print(duplicates)
