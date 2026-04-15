import pandas as pd

df = pd.read_csv('../data/dataset-spotify.csv')
print(df.head())
print(df.info())

#Remove rows that contain empty cells
new_df = df.dropna()

print(new_df.info())

print("Duplicates ")
print(new_df.duplicated())

if new_df.duplicated().sum() > 0:
    print('There are duplicates')
else:
    print('There are no duplicates')




