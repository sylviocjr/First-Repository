### Dec. 31, 2021 - Approaching New Year's Day !!! ###
### The main purpose here is to read two strings and convert both strings to upper case.
### In addition, a little practice of defining and using functions in Python.

### Sylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil ###

def print_words():
    i = 0
    while i <= 1:
        print(words[i], end = " ")
        i+=1


def upper_words():
    i = 0
    while i <= 1:
        words[i] = words[i].upper()
        i+=1

words=[]   ### List of words ###
word_1 = input("Enter first word: ")
words.append(word_1)
word_2 = input("Enter 2nd word: ")
words.append(word_2)

print_words()

print("\nUpper case: ")

upper_words()

print_words()


print("\n\n### Sylvio Carneiro Junior - sylviocjr.dev@gmail.com - Santa Catarina, Brazil ###")

