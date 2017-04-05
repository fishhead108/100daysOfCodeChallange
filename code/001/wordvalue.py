import operator
from data import DICTIONARY, LETTER_SCORES

def load_words(filename):
    """Load dictionary into a list and return list"""
    with open(filename, 'r') as file:
        words = file.read().splitlines()
        return words

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    cost = sum([LETTER_SCORES[x] for x in word.upper() if x.isalpha()])
    return cost

def max_word_value(wordlist=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if wordlist is None:
        wordlist = load_words(DICTIONARY)

    words_with_price = {}

    for word in wordlist:
        words_with_price[word] = calc_word_value(word)

    highest_word = max(words_with_price.items(), key=operator.itemgetter(1))[0]
    return highest_word



if __name__ == "__main__":
    mywords = load_words(DICTIONARY)
    print(max_word_value(mywords))