"""
An implementation of Grammar 4.25 from the Dragon Book

This grammar is ambiguous and needs some resolution
heuristics, since it's also useful.
"""

# flake8: noqa


def make_g(Grammar=None, compile=True):
    grammar = Grammar()
    n = grammar.nt


    @n.E ( n.E, 'sub', n.E, 'sup', n.E )
    def f(e1, sub, e2, sup, e3):
        return "({} sub {} sup {})".format(e1, e2, e3)

    @n.E ( n.E, 'sub', n.E )
    def f(e1, sub, e2):
        return "({} sub {})".format(e1, e2)

    @n.E ( n.E, 'sup', n.E )
    def f(e1, sup, e2):
        return "({} sup {})".format(e1, e2)

    @n.E ( '{', n.E, '}' )
    def f(_1, e, _2):
        return e

    @n.E ( 'x' )
    def x(_):
        return "x"


    if compile:
        grammar.compile(start=n.E)

    return grammar
