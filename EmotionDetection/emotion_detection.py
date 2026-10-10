"""Módulo de detección de emociones basado en el servicio Watson NLP.

Expone la función ``emotion_detector``, que envía un texto al servicio
EmotionPredict de Watson NLP y devuelve las puntuaciones de las cinco
emociones analizadas junto con la emoción dominante.
"""

import json
import requests

URL = ('https://sn-watson-emotion.labs.skills.network/v1/'
       'watson.runtime.nlp.v1/NlpService/EmotionPredict')

HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}


def emotion_detector(text_to_analyse):
    """Analiza el texto recibido y devuelve sus puntuaciones de emoción.

    Args:
        text_to_analyse (str): texto que se desea analizar.

    Returns:
        dict: diccionario con las claves anger, disgust, fear, joy, sadness
        y dominant_emotion. Cuando el servicio responde con el código de
        estado 400, todos los valores del diccionario son None.
    """
    input_json = {"raw_document": {"text": text_to_analyse}}

    response = requests.post(URL, json=input_json, headers=HEADERS, timeout=30)

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    scores = {
        'anger': anger_score,
