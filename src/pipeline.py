import pandas as pd
import matplotlib.pyplot as plt
import cleaning
import analysis
import visualization
from src.ml import prepare_target, split_data, train_model, evaluate_model

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

#grouped_popularity = analysis.popularity(df)
#grouped_popularity.to_csv("../output/popularity_analysis.csv")




#with pd.ExcelWriter("../output/report.xlsx") as writer:
#       df.to_excel(writer, sheet_name="cleaned data", index=False)
#       grouped_tempo.to_excel(writer, sheet_name="grouped analysis", index=True, startrow=1)
#       grouped_energy.to_excel(writer, sheet_name="grouped analysis", index=True, startrow=10)
       #grouped_popularity.to_excel(writer, sheet_name="grouped analysis", index=True, startrow=20)


visualization.bar_chart(grouped_tempo, "tempo.png", "Tempo vs. popularity")
visualization.bar_chart(grouped_energy, "energy.png", "Energy vs. popularity")
#visualization.bar_chart(grouped_popularity, "popularity.png", "Popularity in general")

df = prepare_target(df)
X_train, X_test, y_train, y_test = split_data(df)
model = train_model(X_train, y_train)
accuracy, report, matrix = evaluate_model(model, X_test, y_test)

with open("../output/ml_result.txt", "w") as text_file:
       text_file.write(f"Accuracy: {str(accuracy)}")
       text_file.write("\n")
       text_file.write(f"Classification report \n {str(report)}")
       text_file.write("\n")
       text_file.write(f"Confusion matrix \n {str(matrix)}")


