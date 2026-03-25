import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dataset-spotify.csv')
new_df = df.dropna()

#High vs. low popularity analysis
high_popularity_df = new_df[new_df['popularity'] > 70]
low_popularity_df =new_df[new_df['popularity']<30]
print(f"high popularity: {high_popularity_df}")
print(f"low popularity: {low_popularity_df}")

mean_value_high = high_popularity_df[['energy', 'instrumentalness', 'loudness', 'danceability' ]].mean()
mean_value_low = low_popularity_df[['energy', 'instrumentalness', 'loudness', 'danceability' ]].mean()

plt.rcParams["figure.figsize"] = (10,6)

plt.subplot(2,2,1)
plt.bar( ['high popularity', 'low popularity'],
         [mean_value_high['energy'], mean_value_low['energy']], color='blue', width=0.5)
plt.ylabel('Energy')

plt.subplot(2,2,2)
plt.bar( ['high popularity', 'low popularity'],
         [mean_value_high['loudness'], mean_value_low['loudness']], color='red', width=0.5)
plt.ylabel('Loudness')

plt.subplot(2,2,3)
plt.bar( ['high popularity', 'low popularity'],
         [mean_value_high['danceability'], mean_value_low['danceability']], color='green', width=0.5)
plt.ylabel('Danceability')

plt.subplot(2,2,4)
plt.bar( ['high popularity', 'low popularity'],
         [mean_value_high['instrumentalness'], mean_value_low['instrumentalness']], color='orange', width=0.5)
plt.ylabel('Instrumentalness')

plt.show()

#Conclusions: The higher the danceability, the higher th popularity is
#The higher the loudness, the higher the popularity
#The higher the energy, the more popular the track is
#The higher the instrumentalness is, the less popular the track is