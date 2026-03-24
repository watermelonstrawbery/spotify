import pandas as pd

df = pd.read_csv('dataset-spotify.csv')
new_df = df.dropna()

print('Mean values')
print(new_df[['popularity', 'energy']].mean(numeric_only=True))
