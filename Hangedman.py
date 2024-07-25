import random

words = ["python", "hangman", "computer", "programming", "challenge"]

def Chosen():
    return random.choice(words)

def line_letter(chosen_words):
    n = len(chosen_words)
    sample = []
    for x in range(n):
        sample.append('_')
    return sample


def display(words,guessed_letters):
    display = ''
    for x in words:
        if x in guessed_letters:
            display += x
        else:
            display += '_'
    return display


def guess():
    print('Welcome to Hangedman')
    chosen_words = Chosen()
    guess_letter = []
    attempts = 0
    while(True):
        print(display(chosen_words,guess_letter))
        something = input("Pick Your Guess: ")
        if(something.isalpha() and len(something) == 1):
            if(something in chosen_words):
                guess_letter.append(something)
                print("Good Guess")
                if(set(chosen_words).issubset(set(guess_letter))):
                    print(display(chosen_words,guess_letter))
                    print("You are the Winnder")
                    break
                else:
                    continue
            else:
                attempts += 1
                print("You've Guessed Wrong")
                if(attempts == 10):
                    print("YOU LOSE!")
                    break
        else:
            print("That's invalid answer!")
            continue

guess()