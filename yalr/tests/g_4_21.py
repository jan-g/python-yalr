"""
An implementation of Grammar 4.21 from the Dragon Book

This grammar is ambiguous, but is LR(1)
"""

# flake8: noqa


def make_g(Grammar=None, compile=True):
    grammar = Grammar()
    n = grammar.nt

    @n.S_(n.S)
    def f(*s):
        pass

    @n.S(n.C, n.C)
    def f(*s):
        pass

    @n.C('c', n.C)
    def f(*s):
        pass

    @n.C('d')
    def f(*s):
        pass

    if compile:
        grammar.compile(start=n.S_, augment=False)

    return grammar
