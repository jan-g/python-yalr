"""
An implementation of Grammar 4.19 from the Dragon Book
"""

# flake8: noqa


def make_g(Grammar=None, compile=True):
    grammar = Grammar()
    n = grammar.nt

    @n.E_(n.E)
    def f(e):
        pass

    @n.E(n.E, '+', n.T)
    def f(e, _, t):
        pass

    @n.E(n.T)
    def f(t):
        pass

    @n.T(n.T, '*', n.F)
    def f(t, _, f):
        pass

    @n.T(n.F)
    def f(f):
        pass

    @n.F('(', n.E, ')')
    def f(_1, e, _2):
        pass

    @n.F(str)
    def f(id):
        pass

    if compile:
        grammar.compile(start=n.E_, augment=False)

    return grammar
