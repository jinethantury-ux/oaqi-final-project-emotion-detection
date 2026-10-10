"""Servidor Flask de la aplicación Detector de Emociones.

Expone la interfaz web y el punto final que analiza el texto enviado por
el usuario mediante el paquete EmotionDetection.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emot_detector():
    """Analiza el texto recibido y devuelve las emociones detectadas.

    Returns:
        str: cadena con las puntuaciones de cada emoción y la emoción
        dominante, o un mensaje de error cuando la entrada no es válida.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


@app.route("/")
def render_index_page():
    """Muestra la página principal de la aplicación.

    Returns:
        str: contenido renderizado de la plantilla index.html.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
