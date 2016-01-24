import pytest

from .. import SLR as Grammar, GrammarError


def make_g():
    grammar = Grammar()
    n = grammar.nt

    @n.A(n.A, 'b')
    def f(stack):
        print("A -> Ab")
        return None

    @n.A('c')  # noqa
    def f(stack):
        print("A -> c")

    grammar.compile(start=n.A)

    return grammar


def test_compile():
    grammar = make_g()  # noqa


def test_compile2():
    g2 = Grammar()
    n2 = g2.nt

    @n2.A(n2.B, 'b')
    def f(stack):
        print("A -> Ab")
        return None

    with pytest.raises(GrammarError):
        g2.compile(start=n2.A)
