"""
Fraud Detection Model Testing

This script loads a pre-trained fraud detection model and its associated
TF-IDF vectorizer. It allows users to input a transcript and receive a
fraud prediction.

Usage:
    Run the script and provide a transcript to check if it is fraudulent.
"""

import joblib


def load_model():
    """
    Load the trained fraud detection model and TF-IDF vectorizer.

    Returns:
        tuple: Loaded model and vectorizer.
    """
    model = joblib.load("fraud_detection_model.pkl")
    vectorizer = joblib.load("tfidf_vectorizer.pkl")
    return model, vectorizer


def predict_fraud(transcript, model, vectorizer):
    """
    Predict whether a given transcript is fraudulent or not.

    Args:
        transcript (str): The input call transcript.
        model (LogisticRegression): The trained fraud detection model.
        vectorizer (TfidfVectorizer): The trained TF-IDF vectorizer.

    Returns:
        str: "Fraudulent" if detected as fraud, otherwise "Non-Fraudulent".
    """
    x_new = vectorizer.transform([transcript])
    prediction = model.predict(x_new)[0]
    return "Fraudulent" if prediction == 1 else "Non-Fraudulent"


def main():
    """
    Main function to test the fraud detection model with an example transcript.
    """
    model, vectorizer = load_model()
    # transcript = "Please confirm your OTP to secure your bank account."
    transcript = "This is your doctor calling about your appointment."
    prediction = predict_fraud(transcript, model, vectorizer)
    print(f"Prediction: {prediction}")


if __name__ == "__main__":
    main()
