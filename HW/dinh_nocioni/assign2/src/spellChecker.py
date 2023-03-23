import requests


def getResponse(word):
    URL = f"http://agilec.cs.uh.edu/spell?check={word}" 

    return requests.get(URL).text

    
def is_spelling_correct(word): 
    return getResponse(word) == "true"
