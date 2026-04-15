import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../data/dataset-spotify.csv')
new_df = df.dropna()

slow_songs = new_df[new_df['tempo'] < 90]
medium_tempo_songs = new_df[(new_df['tempo'] > 90) & (new_df['tempo'] < 120)]
fast_songs = new_df[new_df['tempo'] > 120]

popularity_slow = slow_songs['popularity'].mean()
popularity_medium = medium_tempo_songs['popularity'].mean()
popularity_fast = fast_songs['popularity'].mean()

print(popularity_slow)
print(popularity_medium)
print(popularity_fast)



plt.bar(['slow songs', 'medium tempo songs', 'fast songs'],[popularity_slow,popularity_medium,popularity_fast])
plt.ylabel('tempo')
plt.xlabel('popularity')

plt.show()

#Conclusion: The faster the tempo, the more popular the song is

