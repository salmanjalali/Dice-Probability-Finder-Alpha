import random, math
from Tkinter import *

class Application (Frame):
    def __init__ (self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.request = Label(self, text = "Please enter the number of Die you want: ")
        self.request.grid()
        
        self.numberBox = Entry(self)
        self.numberBox.grid()

        self.go = Button(self, text = "Go", command = self.reveal)
        self.go.grid()
        
         
    def reveal(self):
        self.request2 = Label(self, text = "Please enter the size of each Die: ")
        self.request2.grid()
        self.numberEntered = int(self.numberBox.get())
        self.sizeEntered = []
        for i in range(0, self.numberEntered):
            self.sizeEntered.append(Entry(self))
            self.sizeEntered[i].grid(row = 4, column = i)
        self.submit = Button(self, text = "Calculate", command = self.answer)
        self.submit.grid()

    def answer(self):
        self.answerBox = Text(self, width = 50, height = 5, wrap = WORD)
        self.answerBox.grid()
        self.answerBox.insert("1.1", "HIII") 
        self.sizeReceived = []
        for j in range(0, self.numberEntered):
            self.sizeReceived.append(self.sizeEntered[j].get())
            probabilities = "Die " + str(j+1) + ": " + str(randomGenerator(self.sizeEntered[j]))
            self.answerBox.insert("%d.%d" % (j, 2), probabilities)


def randomGenerator(size):
    return random.randrange(size)

def main():
    root = Tk()
    root.title("Dice Probability Finder")
    root.geometry("300x100")
    app = Application(root)
    root.mainloop()

main()
