from words import words
import string
import random

def get_word(words):
    word = random.choice(words)
    return word.upper()
#print(get_word(words))

def hangman():
    word = get_word(words)
    word_letters = set(word)
    alphabets = set(string.ascii_uppercase)
    used_letters = set()
    
    while len(word_letters)>0:
        print("Used letters: ",' '.join(used_letters)) #shows the letters already used by the user

        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("Current word: ",' '.join(word_list))

        user_input = input("Enter an Alphabet: ").upper()
        
        if user_input in alphabets - used_letters:
            used_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)
        elif user_input in used_letters:
            print("You have already guessed the letter!")
        else:
            print("Wrong character! Try again")

hangman()
print("Congratulations you guessed the word!")