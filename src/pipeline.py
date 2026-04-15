import pandas as pd
import cleaning
import analysis


df = pd.read_csv('../data/dataset-spotify.csv')

#clenaing
df = cleaning.clean(df)
df = cleaning.add_columns(df)
df.to_csv("../data/cleaned.csv")

#analysis
grouped_tempo = analysis.popularity_per_tempo_level(df)
grouped_tempo.to_csv("../output/tempo_analysis.csv")

grouped_energy = analysis.popularity_per_energy_level(df)
grouped_energy.to_csv("../output/energy_analysis.csv")

grouped_popularity = analysis.popularity(df)
grouped_popularity.to_csv("../output/popularity_analysis.csv")




with pd.ExcelWriter("../output/report.xlsx") as writer:
    df.to_excel(writer, sheet_name="cleaned data", index=False)
    grouped_tempo.to_excel(writer, sheet_name="grouped analysis", index=True, startrow=1)
    grouped_energy.to_excel(writer, sheet_name="grouped analysis", index=True, startrow=10)
    grouped_popularity.to_excel(writer, sheet_name="grouped analysis", index=True, startrow=20)

