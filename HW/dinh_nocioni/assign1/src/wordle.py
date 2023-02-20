import enum

class Match(enum.Enum):
  EXACT = "EXACT"
  EXISTS = "EXISTS"
  NO_MATCH = "NO_MATCH"

class Status(enum.Enum):
  WIN = "WIN"
  IN_PROGRESS = "IN_PROGRESS"
  LOSS = "LOSS"


def tally(target, guess):
    if len(guess) != len(target):
        raise ValueError("Incorrect Size")
        
    return [tallyForPosition(position, target, guess) for position in range(len(target))]

def tallyForPosition(position, target, guess):
    if target[position] == guess[position]:
        return Match.EXACT
    
    letterAtPosition = guess[position]
    
    positionalMatches = countPositionalMatches(target, guess, letterAtPosition)
    nonPositionalOccurrencesInTarget = countNumberOfOccurrenceeUntilPosition(len(target) - 1, target, letterAtPosition) - positionalMatches
    numberOfOccurancesInGuessUntilPosition = countNumberOfOccurrenceeUntilPosition(position, guess, letterAtPosition)

    return Match.EXISTS if nonPositionalOccurrencesInTarget >= numberOfOccurancesInGuessUntilPosition else Match.NO_MATCH

def countPositionalMatches(target, guess, letter):
    return [i if i == j else None for i, j in zip(target, guess)].count(letter)
    
def countNumberOfOccurrenceeUntilPosition(position, word, letter):
    return [letter if word[i] == letter else None for i in range(position + 1)].count(letter)

def message(attempts): 
    return ["Amazing", "Splendid", "Awesome"][attempts] if attempts < 3 else "Yay"

def play(target, guess, attempt):
  status = getStatus(target, guess, attempt)
  print(tally(target, guess))
  return (attempt + 1,
          tally(target, guess),
          status,
          message(attempt) if status == Status.WIN else f"It was {target}, better luck next time" if status == status.LOSS else "")

def getStatus(target, guess, attempt):
   return Status.WIN if target == guess else Status.IN_PROGRESS
  #return Status.WIN if target == guess else Status.LOSS if attempt == 5 else Status.IN_PROGRESS