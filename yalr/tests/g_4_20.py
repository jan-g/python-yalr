"""
An implementation of Grammar 4.20 from the Dragon Book

This grammar is unambiguous, but not SLR.
"""

# flake8: noqa


def make_g(Grammar=None, compile=True):
    grammar = Grammar()
    n = grammar.nt

    @n.S(n.L, '=', n.R)
    def f(*s):
        pass

    @n.S(n.R)
    def f(*s):
        pass

    @n.L('*', n.R)
    def f(*s):
        pass

    @n.L(str)
    def f(*s):
        pass

    @n.R(n.L)
    def f(*s):
        pass

    if compile:
        grammar.compile(start=n.S)

    return grammar
