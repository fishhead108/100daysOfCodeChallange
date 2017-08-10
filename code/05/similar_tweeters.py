import sys
import re
import itertools
import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer

from usertweets import UserTweets

def similar_tweeters(user1, user2):
    userTweets1 = UserTweets(user1)
    userTweets2 = UserTweets(user2)

    nltk.download('punkt')  # if necessary...

    stemmer = nltk.stem.porter.PorterStemmer()
    remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

    def stem_tokens(tokens):
        return [stemmer.stem(item) for item in tokens]

    '''remove punctuation, lowercase, stem'''

    def normalize(text):
        return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

    vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')


    def cosine_sim(text1, text2):
        tfidf = vectorizer.fit_transform([text1, text2])
        return ((tfidf * tfidf.T).A)[0, 1]


    for tweet1 in userTweets1._tweets:
        for tweet2 in userTweets2._tweets:

            clean_text1 = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|(RT|Python)", " ", tweet1.text).split())
            clean_text2 = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|(RT|Python)", " ", tweet2.text).split())

            if len(clean_text1.split()) and len(clean_text2.split()) > 3:
                try:
                    score = cosine_sim(clean_text1, clean_text2)
                except ValueError as err:
                    print(err)
                    print(f'Before {tweet1.text}, after {clean_text1}')
                    print(f'Before {tweet2.text}, after {clean_text2}')
                    continue

                if score > 0.5:
                    print(f'Score was {score}\nUserText1 is {clean_text1}\nUserText2 is {clean_text2}')


    # for i in range(1, 90):
    #     yield from list(itertools.permutations(draw, i))

if __name__ == "__main__":
    # if len(sys.argv) < 3:
    #     print('Usage: {} <user1> <user2>'.format(sys.argv[0]))
    #     sys.exit(1)
    #
    # user1, user2 = sys.argv[1:3]
    user1 = 'techmoneykids'
    user2 = 'pybites'
    similar_tweeters(user1, user2)
