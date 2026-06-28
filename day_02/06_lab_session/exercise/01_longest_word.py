from itertools import count
from logging import log


def get_longest_word(text):
    """TODO: Add decoding process"""
    longest_word = None
    count_longest_word = 0
    for a in text.split():
        count_word = len(a)
        if count_word > count_longest_word:
            longest_word = a
            count_longest_word = count_word

    return longest_word


# "The quick brown fox jumps" -> "quick"
print(get_longest_word("The quick brown fox jumps"))

# "I love programming in Python!" -> "programming"
print(get_longest_word("I love programming in Python!"))

# "" -> ""
print(get_longest_word(""))
