import requests
import json

def emotion_detector(text_to_analyze):
    # Endpoint URL and headers
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    
    # Input JSON
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    # Making the POST request
    try:
        response = requests.post(url, json=input_json, headers=headers)
        response.raise_for_status()  # Raise exception for HTTP errors
        formatted_response = json.loads(response.text)
        emotions = formatted_response["emotionPredictions"][0]["emotion"]
        emotions["dominant_emotion"] = max(emotions, key=emotions.get)
        return emotions
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
