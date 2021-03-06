#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import itertools
import random
from collections import Counter

from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7


def draw_letters():
    """Pick NUM_LETTERS letters randomly. Hint: use stdlib random"""
    return [POUCH[random.randint(0, len(POUCH), )] for _ in range(NUM_LETTERS)]
    # I definitely need to read the documentation :D
    """
    return random.sample(POUCH, NUM_LETTERS)
    """


def input_word(draw):
    """Ask player for a word and validate against draw.
    Use _validation(word, draw) helper."""
    user_word = input("Form a valid word: ")
    if _validation(user_word, draw):
        return user_word
    else:
        return ''
    """
    #Answer:
    while True:
        word = input('Form a valid word: ').upper()
        if not set(word) < set(draw):
            print('One or more characters not in draw, try again')
            continue
        elif not word.lower() in DICTIONARY:
            print('Not a valid dictionary word, try again')
            continue
        return word
    """


def _validation(word, draw):
    """Validations: 1) only use letters of draw, 2) valid dictionary word"""
    count_word = dict(Counter(word))
    count_draw = dict(Counter(draw))

    if word.isnumeric():
        raise ValueError

    elif [char for char in word if char.upper() not in draw]:
        raise ValueError

    elif list(word) == draw:
        raise ValueError

    elif [count_word[w] for w in count_draw if w in count_word and count_word[w] > 1]:
        raise ValueError

    if len([char for char in word if char.upper() in draw]) == len(word):
        if word.lower() in DICTIONARY:
            return True
        else:
            raise ValueError

    """
    Answer:
    for char in word.upper():
        if char in draw:
            draw.remove(char)
        else:
        raise ValueError("{} is not a valid word!".format(word))
    if not word.lower() in DICTIONARY:
        raise ValueError('Not a valid dictionary word, try again')
    return word
    """


# From challenge 01:
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# Below 2 functions pass through the same 'draw' argument (smell?).
# Maybe you want to abstract this into a class?
# get_possible_dict_words and _get_permutations_draw would be instance methods.
# 'draw' would be set in the class constructor (__init__).
def get_possible_dict_words(draw):
    """Get all possible words from draw which are valid dictionary words.
    Use the _get_permutations_draw helper and DICTIONARY constant"""
    word_in_dict = [word for word in _get_permutations_draw(draw) if word.lower() in DICTIONARY]
    if word_in_dict:
        return word_in_dict
    else:
        return ''


def _get_permutations_draw(draw):
    """Helper for get_possible_dict_words to get all permutations of draw letters.
    Hint: use itertools.permutations"""
    # return [''.join(x) for x in itertools.permutations(draw)]
    """
    for i in range(1, 8):
        yield from list(itertools.permutations(draw, i))
    """
    my_dict = []
    for n in range(1, NUM_LETTERS + 1):
        for xs in itertools.permutations(draw, n):
            my_dict.append(''.join(xs))

    return my_dict


# From challenge 01:
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def main():
    """Main game interface calling the previously defined methods"""
    draw = draw_letters()
    print('Letters drawn: {}'.format(', '.join(draw)))

    word = input_word(draw)
    word_score = calc_word_value(word)
    print('Word chosen: {} (value: {})'.format(word, word_score))

    possible_words = get_possible_dict_words(draw)

    max_word = max_word_value(possible_words)
    max_word_score = calc_word_value(max_word)
    print('Optimal word possible: {} (value: {})'.format(
        max_word, max_word_score))

    game_score = word_score / max_word_score * 100
    print('You scored: {:.1f}'.format(game_score))


if __name__ == "__main__":
    main()
