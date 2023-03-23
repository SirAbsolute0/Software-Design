import requests
import random as rnd
import time

def getResponse():
    URL = "https://agilec.cs.uh.edu/words"
    
    return requests.get(URL).text

def parse(response):
    if not (response[0] == '[' and response[-1] == ']'):
        raise ValueError("Not a word list")

    return response[1:-1].replace(' ', '').replace(',', ' ').split()


def get_a_random_word_given_a_seed(seed, words):
    if not hasattr(get_a_random_word_given_a_seed, "seed") or get_a_random_word_given_a_seed.seed != seed:
        get_a_random_word_given_a_seed.seed = seed
        rnd.seed(seed)
        
    return rnd.choice(words)

def get_a_random_word():
    word = get_a_random_word_given_a_seed(time.time(), parse(getResponse()))
    
    if len(word) != 5:
        raise ValueError("Word is not 5 characters long")
    
    return word.upper()
