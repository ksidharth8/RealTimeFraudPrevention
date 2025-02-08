"""
Scam Call Detection API

This script provides a Flask-based API to analyze audio files
using OpenAI's Whisper for speech-to-text transcription and
spaCy for fraud detection based on scam-related keywords.

Endpoints:
    - `/` (GET): Home route with a welcome message.
    - `/analyze` (POST): Accepts a base64-encoded audio file,
      transcribes it, and detects scam content.
"""

import os
import io
import base64
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
import spacy
import whisper
import joblib

# Setup logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
CORS(app)  # Enable CORS

# Load models
nlp = spacy.load("en_core_web_sm")
model = whisper.load_model("base")

# Load the trained fraud detection model and vectorizer
model_fraud = joblib.load("./model/fraud_detection_model.pkl")
vectorizer = joblib.load("./model/tfidf_vectorizer.pkl")  # Load the vectorizer

# Set a max file size limit (in MB)
MAX_AUDIO_SIZE_MB = 5


def transcribe_audio(audio_base64):
    """
    Convert base64-encoded audio to text using Whisper.

    Args:
        audio_base64 (str): Base64 encoded audio file.

    Returns:
        str: Transcribed text or error message.
    """
    try:
        # Decode base64
        audio_bytes = base64.b64decode(audio_base64)

        # Check file size limit
        if len(audio_bytes) > MAX_AUDIO_SIZE_MB * 1024 * 1024:
            return "File too large. Max size is 5MB"

        audio_buffer = io.BytesIO(audio_bytes)  # Use memory instead of files
        result = model.transcribe(audio_buffer)

        return result["text"]
    except (base64.binascii.Error, ValueError, RuntimeError) as e:
        return f"Error: {str(e)}"


# # Fraud detection using spaCy
# def detect_fraud(transcript):
#     """
#     Detect fraud in the transcript using NLP.

#     Args:
#         transcript (str): The transcribed text.

#     Returns:
#         bool: True if fraud detected, False otherwise.
#     """
#     doc = nlp(transcript.lower())

#     scam_keywords = {
#         "otp", "bank account", "remote access", "password", "credit card"
#     }
#     is_fraudulent = any(word in transcript.lower() for word in scam_keywords)

#     # Check named entities (organizations)
#     for ent in doc.ents:
#         if ent.label_ == "ORG" and "bank" in ent.text.lower():
#             is_fraudulent = True

#     # Check for urgency indicators
#     for token in doc:
#         urgent_words = {"urgent", "immediate"}
#         if token.text in urgent_words and token.dep_ in {"advmod", "amod"}:
#             is_fraudulent = True

#     return is_fraudulent

# Fraud detection using our trained model
def detect_fraud(transcript):
    """
    Detect fraud in the transcript using the trained model.

    Args:
        transcript (str): The transcribed text.

    Returns:
        int: 1 if fraud detected, 0 otherwise.
    """
    # Convert the transcript to TF-IDF features
    x_new = vectorizer.transform([transcript])

    # Predict using the trained model
    is_fraudulent = model.predict(x_new)[0]

    return is_fraudulent


@app.route('/analyze', methods=['POST'])
def analyze_audio():
    """
    API endpoint to analyze audio and detect fraud.

    Returns:
        dict: JSON response with transcript and fraud detection result.
    """
    try:
        logging.info("Received audio for analysis.")
        audio_data = request.json.get('audio')

        if not audio_data:
            return jsonify({"error": "No audio data provided"}), 400

        transcript = transcribe_audio(audio_data)
        is_fraudulent = detect_fraud(transcript)

        return jsonify({
            "transcript": transcript,
            "is_fraudulent": is_fraudulent
        })
    except (KeyError, TypeError, ValueError) as e:
        logging.error("Error in analyze_audio: %s", e)
        return jsonify({"error": str(e)}), 500


@app.route("/", methods=["GET"])
def home():
    """
    API Home Route.

    Returns:
        dict: Welcome message.
    """
    return jsonify({
        "message": "Welcome to the Fraud Detection API! "
                   "Use /analyze with POST requests."
    })


if __name__ == '__main__':
    app.run(port=5001, debug=True)
