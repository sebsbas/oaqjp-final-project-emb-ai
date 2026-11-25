import unittest
from EmotionDetection import emotion_detector

class TestEmotion(unittest.TestCase): 

    def test1(self): 
        self.assertEqual(emotion_detector("I am glad this happenedI am glad this happened"), ['joy']) #joy
        self.assertEqual(emotion_detector("I am really mad about thisI am really mad about this"), ['anger']) #anger
        self.assertEqual(emotion_detector("I feel disgusted just hearing about this"), ['disgust']) # disgust
        self.assertEqual(emotion_detector("I am so sad about this"), ['sadness']) # sadness
        self.assertEqual(emotion_detector("I am really afraid that this will happen"), ['fear']) # fear
        
        #self.assertNotEqual(square(-3), -9) 


unittest.main()

tests= '''
I am glad this happened 	joy
I am really mad about this 	anger
I feel disgusted just hearing about this 	disgust
I am so sad about this 	sadness
I am really afraid that this will happen 	fear'''