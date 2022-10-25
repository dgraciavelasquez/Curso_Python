import random
import os
from tkinter.tix import IMAGE
def run():
    IMAGE = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

    words=["crema",
    "cafe",
    "estrella",
    "explosion",
    "guitarra"]
    word = random.choice(words)
    spaces = ["_"] * len(word)
    attemps = 6

    while True:
        os.system("clear")
        for character in spaces:
            print(character, end=" ")
        print(IMAGE[attemps])
        letter = input(" elige una letra")

        found = False
        for idx, character in enumerate(word):
            if character == letter:
                spaces[idx] = letter
                found = True
        
        if not found:
            attemps -=1

        if "_" not in spaces:
            os.system("clear")
            print("Ganaste")
            break
            input()

        if attemps == 0:
            os.system("clear")
            print("Perdiste")
            break
            input()

if __name__ == "__main__":
    run()