import pygame
from wordle import play, tally, Match, Status
from spellChecker import is_spelling_correct
from wordPicker import get_a_random_word
import os
import sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()

TARGET = get_a_random_word()
ROWS = 6
COLUMNS = 5

WIDTH = 568
HEIGHT = 668
MARGIN = 10
TOP_MARGIN = 100
BOTTOM_MARGIN = 100
LR_MARGIN = 100
SQ_SIZE = (WIDTH - 4 * MARGIN - 2 * LR_MARGIN)//5

GREEN = "#6aaa64"
YELLOW = "#c9b458"
GREY = "#787c7e"
WHITE = "ffffff"
BLACK = "#000000"
FONT = pygame.font.Font("UIAssets/FreeSansBold.otf", 50)
MESSAGE_FONT = pygame.font.Font("UIAssets/FreeSansBold.otf", 25)

SUBMIT_BUTTON_IMG = pygame.image.load("UIAssets/submitButton.png")
SUBMIT_BUTTON_DISABLED_IMG = pygame.image.load("UIAssets/submitButtonDisabled.png")
RESET_BUTTON_IMG = pygame.image.load("UIAssets/resetButton.png")
BUTTON = pygame.Rect(WIDTH/2 - 60, 550, 120, 40)
    
pygame.display.set_caption("WORDLE")
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

def inputHandler(guesses, userInput, screenMessage):
    submitRow = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type == pygame.KEYDOWN:
            guesses, userInput, submitRow, screenMessage = keyInput(event, guesses, userInput, screenMessage)
        if event.type == pygame.MOUSEBUTTONDOWN:
            guesses, userInput, submitRow, screenMessage = mouseInput(event, guesses, userInput, screenMessage)
              
    return guesses, userInput, submitRow, screenMessage
        
def mouseInput(event, guesses, userInput, screenMessage):
    if BUTTON.collidepoint(event.pos) and len(userInput) == COLUMNS:
        if is_spelling_correct(userInput):
            guesses.append(userInput)
            return guesses, "", True, ""
        else:
            return guesses, userInput, False, "Not a word"
            
    return guesses, userInput, False, ""

def keyboardSubmit(guesses, userInput):
    if is_spelling_correct(userInput):
        guesses.append(userInput)
        return guesses, "", True, ""
    
    return guesses, userInput, False, "Not a word"

def keyboardActionInput(event, guesses, userInput, screenMessage):
    if event.key == pygame.K_BACKSPACE and len(userInput) > 0:
        return guesses, deleteTyping(userInput), False, ""
    if event.key == pygame.K_RETURN and len(userInput) == COLUMNS:
        return keyboardSubmit(guesses, userInput)
    
    return guesses, userInput, False, ""
    
def keyInput(event, guesses, userInput, screenMessage):
    if len(userInput) < COLUMNS and keyIsAlpha(event.key):
        return guesses, userInput + event.unicode.upper(), False, screenMessage
    return keyboardActionInput(event, guesses, userInput, screenMessage)

def keyIsAlpha(key):
    return True if key >= 97 and key <= 122 else False

def displaySquares(x, y):
    square = pygame.Rect(x, y, SQ_SIZE, SQ_SIZE)
    pygame.draw.rect(SCREEN, GREY, square, width = 2)
    return square

def getColor(match):
    return GREEN if match == Match.EXACT else YELLOW if match == Match.EXISTS else GREY

def displayGuess(guesses):
    matches = tally(TARGET, guesses[i])
    pygame.draw.rect(SCREEN, getColor(matches[j]), square)
    letter = FONT.render(guesses[i][j], False, BLACK)
    surface = letter.get_rect(center = (x + SQ_SIZE//2, y + SQ_SIZE//2))
    SCREEN.blit(letter, surface)
    
def displayTyping(userInput):
    letter = FONT.render(userInput[j], False, BLACK)
    surface = letter.get_rect(center = (x + SQ_SIZE//2, y + SQ_SIZE//2))
    SCREEN.blit(letter, surface)
    
def deleteTyping(userInput):
    userInput = userInput[:len(userInput) - 1]
    return userInput

def submitRowFunc(guesses):
    gameInfo = play(TARGET, guesses[-1], len(guesses)-1)
    status = gameInfo['status']
    return gameInfo, status, False

def displayButton(buttonImage):
    SCREEN.blit(buttonImage, BUTTON)

def printScreenMessage(text):
    message = MESSAGE_FONT.render(text, False, BLACK)
    surface = message.get_rect(center = (WIDTH/2, 620))
    SCREEN.blit(message, surface)
    
def endGameButton():
    SCREEN.blit(RESET_BUTTON_IMG, BUTTON)
    
def resetGame():
    return [], "", Status.IN_PROGRESS, get_a_random_word()

def endGameRestart(guesses, userInput, status, screenMessage, TARGET):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)    
        if event.type == pygame.MOUSEBUTTONDOWN:
            guesses, userInput, status, screenMessage, TARGET = endGameResetButton(event, guesses, userInput, status, screenMessage, TARGET)           
    return guesses, userInput, status, screenMessage, TARGET


def endGameResetButton(event, guesses, userInput, status, screenMessage, TARGET):
    if BUTTON.collidepoint(event.pos):
        screenMessage = ""
        guesses, userInput, status, TARGET = resetGame()
        
    return guesses, userInput, status, screenMessage, TARGET

if __name__ == '__main__':
        guesses = []
        userInput = ""
        status = Status.IN_PROGRESS
        screenMessage = ""

        while True:            
            SCREEN.fill("white")
            y = TOP_MARGIN
            for i in range(ROWS):
                x = LR_MARGIN
                for j in range(COLUMNS):
                    square = displaySquares(x, y)
                    if i < len(guesses):
                        displayGuess(guesses)
                    if i == len(guesses) and j < len(userInput):
                        displayTyping(userInput)
                    x += SQ_SIZE + MARGIN
                y += SQ_SIZE + MARGIN

            if(status == Status.IN_PROGRESS):
                guesses, userInput, submitRow, screenMessage = inputHandler(guesses, userInput, screenMessage)
            if submitRow:
                gameInfo, status, submitRow = submitRowFunc(guesses)                 
            if len(guesses) >= ROWS or status != Status.IN_PROGRESS:
                screenMessage = (gameInfo['message'])
                endGameButton()
                guesses, userInput, status, screenMessage, TARGET = endGameRestart(guesses, userInput, status, screenMessage, TARGET)
            if len(userInput) == COLUMNS:
                displayButton(SUBMIT_BUTTON_IMG)
            elif status == Status.IN_PROGRESS:
                displayButton(SUBMIT_BUTTON_DISABLED_IMG)
            printScreenMessage(screenMessage)
                
            pygame.display.flip()
