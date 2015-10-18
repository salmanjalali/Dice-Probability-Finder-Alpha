import random, math
from Tkinter import *

class Application (Frame):
    def __init__ (self, master):
        Frame.__init__(self, master)

        # Calling the following functions right when the constructor is called
        self.grid()
        self.create_widgets()

    # Creates the appropriate widgets for the main question to show up
    def create_widgets(self):
        self.request = Label(self, text = "Please enter the number of Die and the desired number : ")
        self.request.grid(row = 0, column = 0)
        
        self.numberBox = Entry(self)
        self.numberBox.grid(row = 0, column = 1)

        self.numberDesired = Entry(self)
        self.numberDesired.grid(row = 0, column = 2)

        self.go = Button(self, text = "Go", command = self.reveal)
        self.go.grid(row = 0, column = 3)
        
    # Reveals the insertion boxes for sizes
    def reveal(self):
        self.request2 = Label(self, text = "Please enter the size of each Die: ")
        self.request2.grid(row = 1, column = 0)
        self.numberEntered = int(self.numberBox.get())
        self.sizeEntered = [None] * (self.numberEntered)
        for even in range(0, self.numberEntered, 2):
            self.sizeEntered[even] = Entry(self)
            self.sizeEntered[even].grid(row = (even/2)+1,column = 1)
        for odd in range(1, self.numberEntered, 2):
            self.sizeEntered[odd] = Entry(self)
            self.sizeEntered[odd].grid(row = (odd/2)+1, column = 2)
        self.submit = Button(self, text = "Calculate", command = self.answer)
        self.submit.grid()
    
    # Shows the answer after the "GO" button is pressed
    def answer(self):
        self.answerBox = []
        self.sizeReceived = []
        self.randomDice = []
        self.invalid = False
        for i in range(0, self.numberEntered):
            self.sizeReceived.append(self.sizeEntered[i].get())
        for j in range(0, self.numberEntered):
            if self.sizeReceived[j] < self.numberDesired:
                self.invalid = True
        if not self.invalid:
            # Finds the probability
            self.probability = "42" 
            self.answerBox = Label(self, text = "The probability of a "+ str(self.numberDesired.get()) + " is " + self.probability) 
        else:
            self.answerBox = Label(self, text = "The size entry is invalid")
        self.answerBox.grid(row = (self.numberEntered/2)+2, column = 1)
        
# This can be used later on to get a random number within a set...
def randomGenerator(size):
    return random.randrange(size)

def main():
    # Initializing Tkinter
    root = Tk()
    root.title("Dice Probability Finder")
    root.geometry("830x400")
    app = Application(root)

    # Runs the main loop for the UI to show
    root.mainloop()

main()
