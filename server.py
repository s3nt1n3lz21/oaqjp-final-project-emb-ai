"""
This module provides a flask server and form to detect emotions in text.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """
    Renders the emotion detection form
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def emot_detector():
    """
    Detect emotions in some text

    Args:
        textToAnalyze (str): The text to analyze

    Returns:
        A JSON response with the emotions and their scores.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    emotions = emotion_detector(text_to_analyze)

    anger = emotions["anger"]
    disgust = emotions["disgust"]
    fear = emotions["fear"]
    joy = emotions["joy"]
    sadness = emotions["sadness"]
    dominant_emotion = emotions["dominant_emotion"]

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    response = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} "
        f"and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
