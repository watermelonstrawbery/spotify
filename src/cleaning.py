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
#print(df.describe())


#Feature engineering section

def tempo_level(tempo):
    tempo = float(tempo)
    if tempo > float(142):
        return "High tempo"
    elif (tempo > float(71)) & (tempo < float(140)):
        return "Medium tempo"
    elif tempo < float(71):
        return "Low tempo"


def popularity_level(popularity):
    if popularity > 66:
        return "High"
    elif (popularity > 33) & (popularity < 66):
        return "Medium"
    elif popularity < 33:
        return "Low"

def energy_level(energy):
    energy = float(energy)
    if energy > 0.66:
        return "High"
    elif (energy > 0.33) & (energy < 0.66):
        return "Medium"
    elif energy < 0.33:
        return "Low"

#Added a column grouping tempo levels in high, medium and low tempo
df['tempo_level'] = df['tempo'].apply(tempo_level)
df['popularity_level'] = df['popularity'].apply(popularity_level)
df['energy_level'] = df['energy'].apply(energy_level)
print(df)
df.to_csv("../data/cleaned.csv")
