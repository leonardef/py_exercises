# Define a class which has at least two methods:

# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

# Hints:
# Use init method to construct some parameters


class Maiusculo:
    def __init__(self):
        pass

    def getstring(self):
        self.frase = input("Frase: ")

    def printstring(self):
        print(self.frase.upper())


frase = Maiusculo()

print(type(frase))

# frase.getstring()
# frase.printstring()
