import sys
from usertweets import UserTweets
import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer

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


    for idx in range(90):
        score = cosine_sim(userTweets1[idx].text, userTweets2[idx].text)
        if score > 0:
            print(f'Score was {score}\nUserText1 is {userTweets1[idx].text}\nUserText2 is {userTweets2[idx].text}')

if __name__ == "__main__":
    # if len(sys.argv) < 3:
    #     print('Usage: {} <user1> <user2>'.format(sys.argv[0]))
    #     sys.exit(1)
    #
    # user1, user2 = sys.argv[1:3]
    user1 = 'techmoneykids'
    user2 = 'pybites'
    similar_tweeters(user1, user2)
