import pygame
from wordle import play, tally, Match, Status
import os
import sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()

TARGET = "FAVOR"
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

def inputHandler(guesses, userInput):
    submitRow = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type == pygame.KEYDOWN:
            guesses, userInput, submitRow = keyInput(event, guesses, userInput)
        if event.type == pygame.MOUSEBUTTONDOWN:
            guesses, userInput, submitRow = mouseInput(event, guesses, userInput)
              
    return guesses, userInput, submitRow
        
def mouseInput(event, guesses, userInput):
    if BUTTON.collidepoint(event.pos) and len(userInput) == COLUMNS:
        guesses.append(userInput)
        return guesses, "", True
            
    return guesses, userInput, False

def keyboardSubmit(guesses, userInput):
    return guesses, "", True

def keyboardActionInput(event, guesses, userInput):
    if event.key == pygame.K_BACKSPACE and len(userInput) > 0:
        return guesses, deleteTyping(userInput), False
    if event.key == pygame.K_RETURN and len(userInput) == COLUMNS:
        return keyboardSubmit(guesses, userInput)
            
    return guesses, userInput, False
    
def keyInput(event, guesses, userInput):
    if len(userInput) < COLUMNS and keyIsAlpha(event.key):
        return guesses, userInput + event.unicode.upper(), False
    return keyboardActionInput(event, guesses, userInput)

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
    
def endGameMessages(text):
    message = MESSAGE_FONT.render(text, False, BLACK)
    surface = message.get_rect(center = (WIDTH/2, 620))
    SCREEN.blit(RESET_BUTTON_IMG, BUTTON)
    SCREEN.blit(message, surface)
    
def resetGame():
    return [], "", Status.IN_PROGRESS

def endGameRestart(guesses, userInput, status):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)    
        if event.type == pygame.KEYDOWN:
            guesses, userInput, status = endGameReturnKey(event, guesses, userInput, status)
        if event.type == pygame.MOUSEBUTTONDOWN:
            guesses, userInput, status = endGameResetButton(event, guesses, userInput, status)           
    return guesses, userInput, status

def endGameReturnKey(event, guesses, userInput, status):
    if event.key == pygame.K_RETURN:
        endGameMessages("")
        return resetGame()
    return guesses, userInput, status

def endGameResetButton(event, guesses, userInput, status):
    if BUTTON.collidepoint(event.pos):
        endGameMessages("")
        return resetGame()
    return guesses, userInput, status
    

if __name__ == '__main__':
        guesses = []
        userInput = ""
        status = Status.IN_PROGRESS

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
                guesses, userInput, submitRow = inputHandler(guesses, userInput)
            if submitRow:
                gameInfo, status, submitRow = submitRowFunc(guesses)                 
            if len(guesses) >= ROWS or status != Status.IN_PROGRESS:
                endGameMessages(gameInfo['message'])
                guesses, userInput, status = endGameRestart(guesses, userInput, status)
            if(len(userInput) == COLUMNS and spellCheck(userInput) == False):
                endGameMessages('Not a word')
            if len(userInput) == COLUMNS and spellCheck(userInput) == True:
                displayButton(SUBMIT_BUTTON_IMG)
            elif status == Status.IN_PROGRESS:
                displayButton(SUBMIT_BUTTON_DISABLED_IMG)
                
            pygame.display.flip()
