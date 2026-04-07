# import currency converter so that you can convert currency of course
from currency_converter import CurrencyConverter
# import tkinter for gui of the currency conversion
from tkinter import *
# Creating a function so that the button works because you need it to be a function for that for some reason but that makes sense at the same time since well how else would they do it?
def calculateTheCurrency():
    # get the currency that they want to change from from the text box
    fromCurrency = fromCurrencyEntry.get()
    # get the currency that they want to change to from the text box
    toCurrency = toCurrencyEntry.get()
    # get the amount that they want to change from so that we know how much to actually change
    fromCurrencyAmount = amountOfCurrencyEntry.get()
    # make the thing do calculations for us to make it actually do the maths because I cant hard code all the different currencies amounts for this
    toCurrencyAmount = CurrencyConverter().convert(fromCurrencyAmount, fromCurrency ,toCurrency )
    # insert it into the text box dedicated to the amount
    outputEntryBox.insert(0, toCurrencyAmount)
# make the window so that you can have the GUI
root = Tk()
# set a title for the screen
root.title("Currency Conversion App")
# set the window geometry
root.geometry("350x200")
# make a title label
titleLabel = Label(root, text = "Currency Conversion")
# add it to the screen using a grid
titleLabel.grid(columnspan=3,row=0)
# make a label so the users know that this is what they want to change from
fromCurrencyTitleLabel = Label(root, text = "From")
# make it appear on the screen because otherwise its not on the screen and thats bad because the users cant use it if its not in the screen
fromCurrencyTitleLabel.grid(column=0,row=1)
# make an entry so that the users can input the currency because otherwise they cant enter
fromCurrencyEntry = Entry(root, width=10)
# add it to the screen
fromCurrencyEntry.grid(column=1,row=1)
# add a label for the currencie that they want to change to
toCurrencyTitleLabel = Label(root, text = "To")
# add it to the grid
toCurrencyTitleLabel.grid(column=0,row=2)
# add an entry for the amount that they want to change it to
toCurrencyEntry = Entry(root, width=10)
# add it to the grid
toCurrencyEntry.grid(column=1,row=2)
# add a title so that they know this is the amount that they want to change from to the other one
amountOfCurrencyTitleLabel = Label(root, text = "Amount")
# add it to the grid
amountOfCurrencyTitleLabel.grid(column=0,row=3)
# add an entry for the amount of currency they want to change
amountOfCurrencyEntry = Entry(root, width=10)
# add it to the grid
amountOfCurrencyEntry.grid(column=1,row=3)
# add a button so that they can calculate the thing
figureOutAmountButton = Button(root, text = "Calculate", command=calculateTheCurrency)
# add it to the grid
figureOutAmountButton.grid(columnspan=2,row=4)
# add a label to indicate the output
outputEntryBoxTitle = Label(root, text="Output Amount: ")
# add it to the grid
outputEntryBoxTitle.grid(column=0, row=5)
# add an entry so that we can put the output in it
outputEntryBox = Entry(root, width=30)
# add it to the grid
outputEntryBox.grid(columnspan=15,row=6)
# have the main loop to keep the window open
root.mainloop()