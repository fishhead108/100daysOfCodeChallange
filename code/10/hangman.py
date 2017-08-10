from string import ascii_lowercase
import sys

from movies import get_movie as get_word
from graphics import hang_graphics

ASCII = list(ascii_lowercase)
HANG_GRAPHICS = hang_graphics()


def check_input_char(char, finish_word, present_word):
    if char in present_word:
        print("You already know this character")
        return True

    if char in finish_word:
        for index, character in enumerate(finish_word):

            if character == char:
                present_word[index] = character

                if present_word == finish_word:
                    print(f"You WIN !\nAnswer is: {word}")
                    exit(0)

        return True


def main(word):
    finish_word = ([char for char in word])
    present_word = (['_' if c in ASCII else c for c in word])

    while True:

        print("".join(present_word))
        char = (input("Enter the letter: ")).lower()

        if check_input_char(char, finish_word, present_word):
            pass

        else:
            try:
                print(next(HANG_GRAPHICS))
            except StopIteration:
                print("YOU ARE DEAD")
                exit(1)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        word = sys.argv[1]
        word = word.lower()
    else:
        word = get_word()
    main(word)
