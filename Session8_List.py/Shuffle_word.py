import random
word = input("Enter a word: ")
word = list(word)

random.shuffle(word)
for i in word:
    print(i.upper())