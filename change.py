# import currency converter so that you can convert currency of course
from currency_converter import CurrencyConverter
# make a function as to make more modular and add tkinter over this eventually
def askForCurrencyTypeAndAmount():
    # a function in a function for extra modularity (is that even a word?)
    def changeCurrency():
        # convert the currency and save it to a variable
        toCurrencyAmount = CurrencyConverter().convert(fromCurrencyAmount, fromCurrency ,toCurrency )
        # print it out so that you can actually see what it gives you
        print(toCurrencyAmount)
    # ask for what currency they would like to convert from
    print("what would you like to convert from?")
    # save it as a string to a variable
    fromCurrency = str(input())
    # ask what they would like to convert to
    print("what would you like to convert to?")
    # save the input to a variable for later use
    toCurrency = str(input())
    # ask how much of the currency they are converting from they would like to change to the next currency
    print("how much of " + fromCurrency + " would you like to change to " + toCurrency + "?")
    # save that to a variable for later use
    fromCurrencyAmount = int(input())
    # Call the function to change one currency to the next
    changeCurrency()
# call the main function to start the program
askForCurrencyTypeAndAmount()