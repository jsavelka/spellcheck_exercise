"""Spelling Corrector in Python 3; see http://norvig.com/spell-correct.html

Copyright (c) 2007-2016 Peter Norvig
MIT license: www.opensource.org/licenses/mit-license.php

NOTE: Minor modifications by Jaromir Savelka. See the above link for the
original.

Downloaded from https://github.com/norvig/pytudes/blob/master/py/spell.py
"""

from os import path
import re
from collections import Counter


# ------------------------------------------------------------------------------
# Word counts dictionary
#
def words(text):
    return re.findall(r'\w+', text.lower())


WORDS = Counter(words(open(path.join('data', 'big.txt')).read()))
# ------------------------------------------------------------------------------


def probability(word, word_dict_size=sum(WORDS.values())):
    """Probability of `word`."""
    return WORDS[word] / word_dict_size


def correction(word):
    """Most probable spelling correction for word."""
    return max(candidates(word), key=probability)


def candidates(word):
    """Generate possible spelling corrections for word."""
    return (known([word])
            or known(edits1(word))
            or known(edits2(word))
            or [word])


def known(words):
    """The subset of `words` that appear in the dictionary of WORDS."""
    return set(w for w in words if w in WORDS)


def edits1(word):
    """All edits that are one edit away from `word`."""
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)


def edits2(word):
    """All edits that are two edits away from `word`."""
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))


if __name__ == '__main__':
    print(correction('advrnture'))
    print(correction('litogation'))
    print(probability('copyright'))

