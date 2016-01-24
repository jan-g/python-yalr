"""
An implementation of 4.11 from the Dragon Book
"""

# flake8: noqa


def make_g(Grammar=None, compile=True):
    grammar = Grammar()
    n = grammar.nt

    @n.E(n.T, n.E_)
    def f(t, e_):
        pass

    @n.E_('+', n.T, n.E_)
    def f(_, t, e_):
        pass

    @n.E_()
    def f():
        pass

    @n.T(n.F, n.T_)
    def f(f, t):
        pass

    @n.T_('*', n.F, n.T_)
    def f(_, f, t_):
        pass

    @n.T_()
    def f():
        pass

    @n.F('(', n.E, ')')
    def f(_1, e, _2):
        pass

    @n.F(str)
    def f(id):
        pass

    if compile:
        grammar.compile(start=n.E, augment=False)
    return grammar
