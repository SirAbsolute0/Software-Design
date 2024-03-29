import unittest
from unittest.mock import patch
from src.spellChecker import getResponse, is_spelling_correct

class SpellCheckerTests(unittest.TestCase):

  def test_getResponse(self):
      self.assertTrue(len(getResponse("FAVOR")) > 0)
          
  def test_is_spelling_correct_with_correct_spelling(self):

    with patch("src.spellChecker.getResponse") as getResponseMock:
      getResponseMock.return_value = 'true'
      
      self.assertTrue(is_spelling_correct("FAVOR"))
      getResponseMock.assert_called_with("FAVOR")      
  
  def test_is_spelling_correct_with_incorrect_spelling(self):

    with patch("src.spellChecker.getResponse") as getResponseMock:
      getResponseMock.return_value = 'false'

      self.assertFalse(is_spelling_correct("RRRRR"))
      getResponseMock.assert_called_with("RRRRR")

  def test_is_spelling_correct_passes_exception_to_caller(self):

    with patch("src.spellChecker.getResponse") as getResponseMock: 
      getResponseMock.side_effect = RuntimeError

      with self.assertRaises(RuntimeError):
        is_spelling_correct("FAVOR")

     
if __name__ == '__main__': 
  unittest.main()
