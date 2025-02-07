"""
Fraud Detection Model Training

This script loads a dataset of call transcripts, processes the text into
TF-IDF features, trains a logistic regression model to detect fraudulent
calls, and saves the trained model and vectorizer for later use.

Usage:
    Run the script to train and save the model.
"""

import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


def load_data():
    """
    Load the dataset from a CSV file.

    Returns:
        tuple: Features (x) and labels (y).
    """
    df = pd.read_csv("../../datasets/data/transcripts.csv")
    x = df["transcript"]  # Transcripts
    y = df["is_fraudulent"]  # Labels (1 = fraud, 0 = not fraud)
    print("Data loaded successfully:", x.shape, y.shape)
    return x, y


def preprocess_data(x):
    """
    Convert text transcripts into TF-IDF features.

    Args:
        x (pd.Series): Raw text data.

    Returns:
        tuple: Transformed TF-IDF features and the vectorizer.
    """
    vectorizer = TfidfVectorizer()
    x_tfidf = vectorizer.fit_transform(x)
    return x_tfidf, vectorizer


def train_model(x_tfidf, y):
    """
    Train a Logistic Regression model on the preprocessed data.

    Args:
        x_tfidf (sparse matrix): TF-IDF transformed text features.
        y (pd.Series): Labels (1 = fraud, 0 = not fraud).

    Returns:
        LogisticRegression: Trained model.
    """
    model = LogisticRegression()
    model.fit(x_tfidf, y)
    return model


def save_model(model, vectorizer):
    """
    Save the trained model and TF-IDF vectorizer to disk.

    Args:
        model (LogisticRegression): Trained fraud detection model.
        vectorizer (TfidfVectorizer): Trained TF-IDF vectorizer.
    """
    joblib.dump(model, "fraud_detection_model.pkl")
    joblib.dump(vectorizer, "tfidf_vectorizer.pkl")
    print("Model and vectorizer saved successfully!")


def main():
    """
    Main function to train and save the fraud detection model.
    """
    x, y = load_data()
    x_tfidf, vectorizer = preprocess_data(x)
    model = train_model(x_tfidf, y)
    save_model(model, vectorizer)


if __name__ == "__main__":
    main()
