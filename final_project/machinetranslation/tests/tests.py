import unittest

from translator import french_to_english, english_to_french

class TestToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertRaises(ValueError, lambda: english_to_french(None))
        self.assertEqual(english_to_french("Hello"), "Bonjour") 
        

class TestToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertRaises(ValueError, lambda: french_to_english(None))        
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        

unittest.main()