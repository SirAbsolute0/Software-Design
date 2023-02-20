import unittest

from src.wordle import tally, message, play, Match, Status

EXACT = Match.EXACT
EXISTS = Match.EXISTS
NO_MATCH = Match.NO_MATCH

WIN = Status.WIN
IN_PROGRESS = Status.IN_PROGRESS
LOSS = Status.LOSS

class WordleTests(unittest.TestCase):
  
  def test_canary(self):
    self.assertTrue(True)

  def test_tally(self):

    responses = [[[EXACT,    EXACT,    EXACT,    EXACT,    EXACT],    "FAVOR"],
                 [[NO_MATCH, NO_MATCH, NO_MATCH, NO_MATCH, NO_MATCH], "TESTS"],
                 [[EXISTS,   EXACT,    NO_MATCH, NO_MATCH, NO_MATCH], "RAPID"],
                 [[NO_MATCH, EXACT,    NO_MATCH, EXACT,    EXACT],    "MAYOR"],
                 [[NO_MATCH, NO_MATCH, EXACT,    NO_MATCH, EXACT],    "RIVER"],               
                 [[EXISTS,   NO_MATCH, NO_MATCH, NO_MATCH, NO_MATCH], "AMAST"]]
    
    for test in responses:
      response, guess = test
      with self.subTest():
        self.assertEqual(response, tally("FAVOR", guess))

    responses = [[[EXACT,    EXACT,    EXACT,    EXACT,    EXACT],    "SKILL"],
                 [[EXACT,    NO_MATCH, EXACT,    NO_MATCH, EXACT],    "SWIRL"],
                 [[NO_MATCH, EXISTS,   NO_MATCH, NO_MATCH, EXACT],    "CIVIL"],
                 [[EXACT,    NO_MATCH, EXACT,    NO_MATCH, NO_MATCH], "SHIMS"],
                 [[EXACT,    EXISTS,   EXISTS,   EXACT,    NO_MATCH], "SILLY"],
                 [[EXACT,    EXISTS,   EXACT,    NO_MATCH, NO_MATCH], "SLICE"]]

    for test in responses:
      response, guess = test
      with self.subTest():
        self.assertEqual(response, tally("SKILL", guess))

  def test_submitRow_valueExceptions(self):
    responses = [[ValueError, "FOR"],
                 [ValueError, "FERVER"]]

    for test in responses:
      response, guess = test
      with self.assertRaises(response):
        tally("FAVOR", guess)

  def test_play(self):
    response = [[(1, [EXACT, EXACT, EXACT, EXACT, EXACT], WIN, "Amazing"), "FAVOR", 0],
                [(1, [EXISTS, EXACT, NO_MATCH, NO_MATCH, NO_MATCH], IN_PROGRESS, ''), "RAPID", 0]]
    #Feedback: how about the result of play equals {"attempts": 1, "response": ..., "status": WIN, "message": "Amazing"}
    
    for test in response:
      response, guess, attempt = test
      with self.subTest():
        self.assertEqual(response, play("FAVOR", guess, attempt))
    
  def test_playExceptions(self):
      responses = [[ValueError, "FOR", 0]]
    
      for test in responses:
          response, guess, attempt = test
          with self.assertRaises(response):
              play("FAVOR", guess, attempt)
               
if __name__ == '__main__': 
  unittest.main()
