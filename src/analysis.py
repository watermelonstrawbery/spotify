

def popularity_per_tempo_level(df):
    grouped_tempo = df.groupby('tempo_level').agg({
        'popularity': 'mean',
    })
    return grouped_tempo

def popularity_per_energy_level(df):
    grouped_energy = df.groupby('energy_level').agg({
        'popularity': 'mean',
    })
    return grouped_energy

#def popularity(df):
#    grouped_popularity = df.groupby('popularity_level').agg({
      #  'danceability': 'mean',
       # 'loudness': 'mean',
        #'acousticness': 'mean',
       # 'energy': 'mean',
        #'tempo': 'mean',
#    })
#    return grouped_popularity