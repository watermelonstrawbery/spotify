import pandas as pd
import sklearn.model_selection as ms
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def is_popular(popularity):
    if popularity > 60:
        return 1
    else:
        return 0


def prepare_target(df):
    df['is_popular'] = df['popularity'].apply(is_popular)
    return df


def split_data(df):
    X = df[['danceability', 'loudness', 'tempo', 'energy', 'acousticness']]
    y = df['is_popular']

    X_train, X_test, y_train, y_test = ms.train_test_split(
        X, y, test_size=0.20, random_state=23, shuffle=True)

    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train):
    model = LogisticRegression(class_weight='balanced' , max_iter=10000, random_state=0)
    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)

    #print(df[['is_popular']].apply(pd.Series.value_counts))
    #The dataset is highly imbalanced (~88% not popular),
    # which inflates accuracy. This highlights the limitation of
    # using accuracy alone as a metric.

    acc = accuracy_score(y_test, y_pred) * 100
    print(f"Accuracy: {acc:.2f}%")

    report = classification_report(y_test, y_pred)
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    matrix = confusion_matrix(y_test, y_pred)
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    return acc, report, matrix


