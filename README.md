### Spotify Data Analysis & Machine Learning Pipeline

### Overview

This project analyzes Spotify song data and builds a complete data pipeline, from raw data processing to machine learning.

The goal was to explore how audio features (such as energy, tempo, and danceability) relate to song popularity, and to test whether popularity can be predicted using these features.

### Data

The data set used can be found at:
https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset


### Pipeline Steps

## 1. Data Cleaning

- Removed missing values
- Removed unnecessary columns
- Filtered invalid data (e.g. tempo = 0)

## 2. Feature Engineering

Created new categorical features:

- Tempo level (Low / Medium / High)
- Energy level (Low / Medium / High)
- Popularity level

## 3. Data Analysis

Grouped and compared features:

Popularity vs Tempo level
Popularity vs Energy level


## 4. Visualization

Generated bar charts to visualize relationships:

Tempo vs Popularity
Energy vs Popularity

(All charts are saved in `/output/charts`)

## 5. Machine Learning

Built a classification model to predict whether a song is popular.

Model: Logistic Regression
Features: energy, danceability, acousticness, tempo, loudness
Target: 'is_popular' (binary classification)


### Results & Insights

High tempo songs tend to have slightly higher popularity
Medium energy songs performed best on average
Audio features alone show limited correlation with popularity

# Tempo vs Popularity
High tempo songs show slightly higher average popularity compared to medium and low tempo songs. However, the difference between high and medium tempo is small, suggesting a weak overall correlation.

# Energy vs Popularity
Songs with medium and high energy levels tend to be more popular than low energy songs. This indicates a clearer pattern compared to tempo, where higher energy is generally associated with higher popularity.

## Machine Learning Results

Dataset was highly imbalanced (~88% not popular)
Accuracy alone was misleading

After handling imbalance:

Recall (popular songs): 0.63

The model can identify a majority of popular songs, but misses a significant portion.


### Key Learnings

- Data imbalance significantly affects model evaluation
- Accuracy is not always a reliable metric
- Feature engineering and interpretation are critical
- Audio features alone are not enough to predict popularity

### Project Structure

src/

cleaning.py
analysis.py
visualization.py
pipeline.py
ml.py

data/

raw dataset
cleaned dataset

output/

charts
analysis results


### How to Run

Run the pipeline:

pipeline.py

This will:

- clean the data
- generate features
- run analysis
- create visualizations
- train the ML model


### Conclusion

This project demonstrates a full data workflow:
from raw data to insights and machine learning.

While the model shows moderate predictive ability, it highlights the limitations of using only audio features to explain song popularity.
