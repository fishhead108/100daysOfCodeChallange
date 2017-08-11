import os
import fnmatch
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
    dir = os.path.dirname(pat.split('*')[0])
    ext = os.path.basename(pat)
    for path, dirlist, filelist in os.walk(dir):
        for name in fnmatch.filter(filelist, ext):
            yield os.path.join(path, name)


def gen_lines(files):
    for file in files:
        for line in open(file):
            yield line


def gen_grep(lines, pattern):
    patc = re.compile(pattern)
    for line in lines:
        if patc.search(line):
            yield (line.split()[1])


def gen_count(lines):
    lines = collections.Counter(lines).most_common()
    for line in lines:
        name, num = line
        print(f'{num:2} {name.strip(",")}')


if __name__ == "__main__":
    # call the generators, passing one to the other
    files = gen_files('../*/*.py')
    lines = gen_lines(files)
    greps = gen_grep(lines, '^import')
    clean = gen_count(greps)
    print(clean)
