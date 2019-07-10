import random

words_list = ["animal","champion","computer","hacker","game","organization","perspective"]

while True:
    random_word = words_list[random.randint(0, len(words_list)-1)]
    suffled_word = list(random_word)
    random.shuffle(suffled_word)

    print("The suffled word: ",end = "")
    for c in suffled_word:
        print(c,end = " ")

    guess = input("\nGuess the original word: ")
    if guess == random_word:
        print("Correct!")
    else:
        print("Wrong, the answer is", random_word)

    again = input("Play again?(Y/N) ")
    if again == "Y":
        continue
    else:
        break
