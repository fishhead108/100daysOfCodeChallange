from glob import iglob
import re
import collections
"""
Turn the following unix pipeline into Python code using generators

$ for i in ../*/*py; do grep ^import $i|sed 's/import //g' ; done | sort | uniq -c | sort -nr
   4 unittest
   4 sys
   3 re
   3 csv
   2 tweepy
   2 random
   2 os
   2 json
   2 itertools
   1 time
   1 datetime
"""


def gen_files(pat):
    yield from iglob(pat)


def gen_lines(files):
    for file in files:
        with open(file) as f:
            yield from f.readlines()


def gen_grep(lines, pattern):
    patc = re.compile(pattern)
    for line in lines:
        if patc.search(line):
            yield (line.split()[1])


def gen_count(modules):
    yield from collections.Counter(modules).most_common()


if __name__ == "__main__":
    # call the generators, passing one to the other
    files = gen_files('../*/*.py')
    lines = gen_lines(files)
    greps = gen_grep(lines, '^import')
    for mod, count in gen_count(greps):
        print(f'{count:2} {mod.strip(",")}')
