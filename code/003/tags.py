from collections import Counter
from difflib import SequenceMatcher
from itertools import product
import re

IDENTICAL = 1.0
TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87
TAG_HTML = re.compile(r'<category>([^<]+)</category>')


def get_tags():
    """Find all tags (TAG_HTML) in RSS_FEED.
    Replace dash with whitespace.
    Hint: use TAG_HTML.findall"""
    with open(f"./{RSS_FEED}", 'r') as rssfile:
        content = rssfile.readlines()

    return [word.lower() for word in re.findall(TAG_HTML, content[1])]


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags
    Hint: use most_common method of Counter (already imported)"""
    return Counter.most_common(Counter(tags), TOP_NUMBER)


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR
    Hint 1: compare each tag, use for in for, or product from itertools (already imported)
    Hint 2: use SequenceMatcher (imported) to calculate the similarity ratio
    Bonus: for performance gain compare the first char of each tag in pair and continue if not the same"""
    """
    for pair in product(tags, tags):
        pair = tuple(sorted(pair))
        similarity = SequenceMatcher(None, *pair).ratio()
        if SIMILAR < similarity < IDENTICAL:
            yield pair
    """
    return [sorted(pair) for pair in product(tags, repeat=2)
                       if SequenceMatcher(None, *pair).ratio() > SIMILAR
                       and SequenceMatcher(None, *pair).ratio() < IDENTICAL]

if __name__ == "__main__":
    tags = get_tags()
    top_tags = get_top_tags(tags)
    print('* Top {} tags:'.format(TOP_NUMBER))
    for tag, count in top_tags:
        print('{:<20} {}'.format(tag, count))
    similar_tags = dict(get_similarities(tags))
    print()
    print('* Similar tags:')
    for singular, plural in similar_tags.items():
        print('{:<20} {}'.format(singular, plural))
