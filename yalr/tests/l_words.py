""" A lexer that just splits its input up into
    alphanumeric words.
"""

from .. import Lexer


def make_l():
    l = Lexer()

    @l('\s+')
    def whitespace():
        pass

    @l(r'(?P<token> \w+ )')
    def word(token=None):
        return token

    return l
