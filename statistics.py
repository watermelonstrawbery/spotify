import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dataset-spotify.csv')
new_df = df.dropna()

print('Mean values')
print(new_df[['popularity', 'energy']].mean(numeric_only=True))

print(new_df.corr(numeric_only=True))
#popularity and loudness have a correlation of 0.05
#popularity and danceability have a correlation of 0.035
#popularity and instrumentalness have a correlation of -0.09
#These are the strongest correlations among others but they are still weak

plt.rcParams["figure.figsize"] = (10,6)

plt.subplot(2,2,1)
x1 = new_df['popularity']
y1 = new_df['loudness']
plt.scatter(x1,y1,c='r')
plt.grid()


plt.subplot(2,2,2)
x2 = new_df['popularity']
y2 = new_df['danceability']
plt.scatter(x2,y2,c='g')
plt.grid()


plt.subplot(2,2,3)
x3 = new_df['popularity']
y3 = new_df['instrumentalness']
plt.scatter(x3,y3,c='b')
plt.grid()

plt.show()


