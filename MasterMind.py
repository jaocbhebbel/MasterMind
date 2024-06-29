from graphics import *
import copy
import random

#rules for mastermind
#8 turns
#each turn place down 4 "guesses"
#guess is 4 colors
#guesses are compared to some existing key

#if a guess is right color wrong spot
#place a white peg at a correlating position

#if a guess is right color right spot
#place a red peg at a correlating position

#what i need:

#back end
#a data structure containing the key 
#a data structure containing the guesses
#some function to evaluate the guesses and compare with the key


#front end
#draw guesses
#draw results

def buildWin():
    
    win=GraphWin("Mastermind",500,800)

    background = Rectangle(Point(0,0),Point(500,800))

    background.setFill('white')

    background.draw(win)

    Blue = Circle(Point(50,100),20)

    Blue.setFill('blue')

    Green = Circle(Point(50,150),20)

    Green.setFill('green')

    Red = Circle(Point(50,200),20)

    Red.setFill('red')

    Yellow = Circle(Point(50,250),20)

    Yellow.setFill('yellow')

    Black = Circle(Point(50,300),20)

    Black.setFill('black')

    Pink = Circle(Point(50,350),20)

    Pink.setFill('pink')

    Blue.draw(win)

    Green.draw(win)

    Red.draw(win)

    Yellow.draw(win)

    Black.draw(win)

    Pink.draw(win)

    title = Text(Point(250,30),"Master Mind")

    title.setSize(30)

    title.draw(win)


    return win
    
def drawGuess(win, TURN_OFFSET, GUESS_OFFSET):
    
    click = win.getMouse()
    
    #because the x bounds are the same for all colors
    #checking here makes the if statements less ugly
    while click.getX() < 30 or click.getX() > 70:
        print("select a guess by clicking a colored circle on the left")
        click = win.getMouse()
        
    #blue draw
    if 80 <= click.getY() <= 120:
        guess = Circle(Point(180 + GUESS_OFFSET,100 + TURN_OFFSET),20)
        guess.setFill("blue")
        guess.draw(win)
        return "blue"
          
    #green draw
    elif 130 <= click.getY() <= 170:
        guess = Circle(Point(180 + GUESS_OFFSET,100 + TURN_OFFSET),20)
        guess.setFill("green")
        guess.draw(win)
        return "green"
        
    #red draw
    elif 180 <= click.getY() <= 220:
        guess = Circle(Point(180 + GUESS_OFFSET,100 + TURN_OFFSET),20)
        guess.setFill("red")
        guess.draw(win)
        return "red"
        
    #yellow draw
    elif 230 <= click.getY() <= 270:
        guess = Circle(Point(180 + GUESS_OFFSET,100 + TURN_OFFSET),20)
        guess.setFill("yellow")
        guess.draw(win)
        return "yellow"
            
    #black draw
    elif 280 <= click.getY() <= 320:
        guess = Circle(Point(180 + GUESS_OFFSET,100 + TURN_OFFSET),20)
        guess.setFill("black")
        guess.draw(win)
        return "black"
         
    #pink draw
    elif 330 <= click.getY() <= 370:
        guess = Circle(Point(180 + GUESS_OFFSET,100 + TURN_OFFSET),20)
        guess.setFill("pink")
        guess.draw(win)
        return "pink"

    else:
        #if no color selection was made
        #run it again until one is selected
        print("select a guess by clicking a colored circle on the left")
        return drawGuess(win, TURN_OFFSET, GUESS_OFFSET)

def guessPhase(win, TURN_OFFSET):
    
    guesses = ""
    for guessNumber in range(0, 4):
        guesses += drawGuess(win, TURN_OFFSET, GUESS_OFFSET = guessNumber * 50) + " "
        
    guesses.strip()
    playerGuesses = guesses.split(" ")
    
    #for some reason strip isnt removing all whitespace,
    # I get an empty index from splitting so pop to remove it
    playerGuesses.pop()
        
    return playerGuesses

def responsePhase(win, masterCode, playerGuess,TURN_OFFSET):
    copyMasterCode = copy.deepcopy(masterCode)
    copyPlayerGuess = copy.deepcopy(playerGuess)
    
    
    #this first loop gets right color right spot condition
    for guessNumber in range(0, 4):
        #when guessNumber is even, x_off should be -10, +10 when odd
        #when guessNumber is < 3, y_off should be -10, +10 when >= 3    
        X_OFFSET = -10 + (((guessNumber) % 2) * 20)
        Y_OFFSET = -10 + ((guessNumber // 2) * 20)
        
        outline = Circle(Point(380 + X_OFFSET, 100 + TURN_OFFSET + Y_OFFSET),5)
        outline.setOutline("blue")
        outline.draw(win)

        if copyPlayerGuess[guessNumber] == copyMasterCode[guessNumber]:
            #changing these indices to prevent problems with second loop
            #need to be different values to pass the "not in" conditional
            copyMasterCode[copyMasterCode.index(copyPlayerGuess[guessNumber])] = "X"
            copyPlayerGuess[guessNumber] = "x"
                
            redResponse = Circle(Point(380 + X_OFFSET,100 + TURN_OFFSET + Y_OFFSET),5)
            redResponse.setFill("red")
            redResponse.draw(win)
        else:
            continue

    
    #this second loop gets right color wrong spot condition
    for guessNumber in range(0, 4):
        
        #when guessNumber is even, x_off should be -10, +10 when odd
        #when guessNumber is < 3, y_off should be -10, +10 when >= 3
            
        X_OFFSET = 10 * (-1 + 2 * (guessNumber % 2))
        Y_OFFSET = -10 + ((guessNumber // 2) * 20)

        if copyPlayerGuess[guessNumber] not in copyMasterCode:
            continue
        else: 
            #changing to pass "not in" conditional for future cases
            copyMasterCode[copyMasterCode.index(copyPlayerGuess[guessNumber])] = "X"
            
            blackResponse = Circle(Point(380 + X_OFFSET,100 + TURN_OFFSET + Y_OFFSET),5)
            blackResponse.setFill("black")
            blackResponse.draw(win)           
        
def checkWinCondition(masterCode, playerGuess):
    if (masterCode == playerGuess):
        return True
    else:
        return False
        
def writeMasterCode():
    
    allColors = ['blue', 'green', 'red', 'yellow', 'black', 'pink']
    masterCode = ['', '', '', '']
    for color in range(0, 4):
        randomColor = random.randint(0, 5)
        masterCode[color] = allColors[randomColor]
    print(masterCode)
    return masterCode

def main():

    win = buildWin()

    masterCode = writeMasterCode()

    for turnNumber in range(0, 8):
        
        playerGuess = guessPhase(win, TURN_OFFSET = turnNumber * 50)
        
        responsePhase(win, masterCode, playerGuess, TURN_OFFSET = turnNumber * 50)
        
        if checkWinCondition(masterCode, playerGuess):
            print("you won! the game is over")
            break
        else:
            print("you didn't get the code this try." + "\n" + "read the dots on the right to make a better guess" + "\n" + "black dot means right color wrong spot," + '\n' + "and red dot means right color right spot" + "\n" + "read the dots as guesses 1-2 // 3-4")
    

    if checkWinCondition(masterCode, playerGuess):
        pass
    else:
        print("you lost. the game is over")
        
    input("press enter to quit program")
    return None

main()
