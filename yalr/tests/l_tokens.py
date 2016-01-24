""" A lexer that just splits its input up into
    alphanumeric words, numbers, and some
    miscellaneous single-character 'operators'.
"""

from .. import Lexer


def make_l():
    l = Lexer()

    @l('\s+')
    def whitespace():
        pass

    @l(r'( \d+ )')
    def digits(n):
        return int(n)

    @l(r'(?P<token> \w+ )')
    def word(token=None):
        return token

    @l(r'( [+\-*/^&|=(){}\[\]] )')
    def op(x):
        return x

    return l
