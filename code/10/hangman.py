from string import ascii_lowercase
import sys

from movies import get_movie as get_word
from graphics import hang_graphics

ASCII = list(ascii_lowercase)
HANG_GRAPHICS = hang_graphics()


def main(word):
    def check_input_char(char):
        if char in present_word:
            print("You already know this character")
            return True

        if char in finish_word:
            for index, character in enumerate(finish_word):

                if character == char:
                    present_word[index] = character

                    if present_word == finish_word:
                        print(f"You WIN !\nAnswer is: {secret_word}")
                        exit(0)

            return True

    secret_word = word
    finish_word = ([char for char in secret_word])
    present_word = (['_' for char in secret_word])

    while True:

        print("".join(present_word))
        char = input("Enter the letter: ")

        if char in ASCII:

            if check_input_char(char):
                pass

            else:
                try:
                    print(next(HANG_GRAPHICS))
                except StopIteration:
                    print("YOU ARE DEAD")
                    exit(1)

        else:
            print("Wrong character, type another")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        word = sys.argv[1]
    else:
        word = get_word()
    main(word)
