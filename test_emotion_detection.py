"""Pruebas unitarias del paquete EmotionDetection."""

import unittest

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Verifica que emotion_detector identifique la emoción dominante."""

    def test_joy(self):
        """La frase de alegría debe devolver joy como emoción dominante."""
        result = emotion_detector('I am glad this happened')
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger(self):
        """La frase de enfado debe devolver anger como emoción dominante."""
        result = emotion_detector('I am really mad about this')
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust(self):
        """La frase de desagrado debe devolver disgust como dominante."""
        result = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sadness(self):
        """La frase de tristeza debe devolver sadness como dominante."""
        result = emotion_detector('I am so sad about this')
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear(self):
        """La frase de miedo debe devolver fear como emoción dominante."""
        result = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result['dominant_emotion'], 'fear')


if __name__ == '__main__':
    unittest.main()
