# Write a program that accepts a sequence of whitespace separated words
# as input and prints the words after removing all duplicate words and
# sorting them alphanumerically.

# Suppose the following input is supplied to the program:

# hello world and practice makes perfect and hello world again
# Then, the output should be:

# again and hello makes perfect practice world

palavras = input('Palavras: ').split(' ')
tmp = []

for palavra in palavras:
    if palavras.count(palavra) > 1:
        palavras.remove(palavra)
        tmp = palavras
    else:
        tmp = palavras

tmp.sort()
print(tmp)
