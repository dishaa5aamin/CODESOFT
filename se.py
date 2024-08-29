from tkinter import *  
import random  
  
  
guiWindow = Tk()  
guiWindow.title("The Rock Paper Scissors Game")  
guiWindow.geometry("480x480")  
guiWindow.config(bg = "#588C7E")  
guiWindow.resizable(width = False, height = False)  
  
  
heading = Label(  
    guiWindow,  
    text = 'Let\'s play Rock Paper Scissors',  
    font = 'arial 18 bold',  
    bg = 'pink',  
    fg = 'black'  
    ).pack()  
  
  
userInput = StringVar()  
  
subHeading = Label(  
    guiWindow,  
    text = 'Select any ONE from rock, paper, scissors',  
    font = 'calibri 14 bold',  
    bg = 'pink'  
    ).place(  
        x = 35,  
        y = 110  
        )  
  
Entry(  
    guiWindow,  
    font = 'calibri 14',  
    textvariable = userInput,  
    bg = '#FBEFCC'  
    ).place(  
        x = 110,  
        y = 160  
        )  
  
  
compSelection = random.randint(1, 3)  
  
if compSelection == 1:  
    compSelection = 'rock'  
elif compSelection == 2:  
    compSelection = 'paper'  
else:  
    compSelection = 'scissors'  
  

res = StringVar()  
  
def letsPlay():  
    userSelection = userInput.get()  
    if userSelection == compSelection:  
        res.set("It's a Tie! You made a same choice as computer.")  
    elif userSelection == 'rock' and compSelection == 'paper':  
        res.set("Oops! You Lose. Computer selected Paper.")  
    elif userSelection == 'rock' and compSelection == 'scissors':  
        res.set("Congrats! You Win. Computer selected Scissors.")  
    elif userSelection == 'paper' and compSelection == 'scissors':  
        res.set("Oops! You Lose. Computer selected Scissors.")  
    elif userSelection == 'paper' and compSelection == 'rock':  
        res.set("Congrats! You Win. Computer selected Rock.")  
    elif userSelection == 'scissors' and compSelection == 'rock':  
        res.set("Oops! You Lose. Computer selected Rock.")  
    elif userSelection == 'scissors' and compSelection == 'paper':  
        res.set("Congrats! You Win. Computer selected Paper.")  
    else:  
        res.set("Looks like an invalid input! Consider selecting from - rock, paper & scissors")  
  
 
def resetGame():  
    res.set("")  
    userInput.set("")  
  

def exitGame():  
    guiWindow.destroy()  
  
displayResult = Label(  
    guiWindow,  
    textvariable = res,  
    font = 'calibri 12 bold',  
    bg = '#96CEB4'  
    ).place(  
        x = 20,  
        y = 240  
    )  
  
playButton = Button(  
    guiWindow,  
    font = 'calibri 10 bold',  
    text = 'PLAY',  
    padx = 5,  
    bg = 'white',  
    command = letsPlay  
    ).place(  
        x = 100,  
        y = 300  
        )  
  
resetButton = Button(  
    guiWindow,  
    font = 'calibri 10 bold',  
    text = 'RESET',  
    padx = 5,  
    bg = 'white',  
    command = resetGame  
    ).place(  
        x = 200,  
        y = 300  
        )  
  
exitButton = Button(  
    guiWindow,  
    font = 'calibri 10 bold',  
    text = 'EXIT',  
    padx = 5,  
    bg = 'white',  
    command = exitGame  
    ).place(  
        x = 300,  
        y = 300  
        )  
  
guiWindow.mainloop()  