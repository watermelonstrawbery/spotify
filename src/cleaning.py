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
#print(duplicates)

description = df.describe()
#print(description)
#looks like tempo includes zero which is not reasonable
#those rows should be deleted since they do not represent valid tempo values

#157 rows included 0 in tempo
#df = df[df['tempo'] == 0.0]

#The 157 rows were filtered out
df = df[df['tempo'] > 0.0]
#print(df)
print(df.describe())
