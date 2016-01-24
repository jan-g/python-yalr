""" More complex tests of associativity

    A grammar with + and * (left and right assoc resp)
    cannot be simply resolved: reduce/reduce error.

    A grammar with + and * (both left assoc)
    should give rise to a reduce/reduce error also.

    A grammar with a higher-precedence *
    (left or right assoc) should resolve correctly.
"""

import pytest

from .. import LR1, GrammarError
from .test_associativity import make_l


def make_g(Grammar=LR1, compile=True, assoc=None):
    g = Grammar()
    if assoc is not None:
        assoc(g)
    n = g.nt

    @n.E(str)
    def _(id):
        return id

    @n.E(n.E, '+', n.E)
    def plus(e1, _, e2):
        return "({} + {})".format(e1, e2)

    @n.E(n.E, '*', n.E)
    def splat(e1, _, e2):
        return "({} * {})".format(e1, e2)

    if compile:
        g.compile(start=n.E)

    return g


def test_non_assoc_equal():
    l = make_l()  # noqa

    def assoc(g):
        g.nonassoc('+', '*')

    g = make_g(assoc=assoc)

    with pytest.raises(GrammarError):
        assert g.parse(l.lex("a + b + c")) == '(a + (b + c))'

    with pytest.raises(GrammarError):
        assert g.parse(l.lex("a * b + c")) == '(a * (b + c))'

    with pytest.raises(GrammarError):
        assert g.parse(l.lex("a + b * c")) == '(a + (b * c))'

    with pytest.raises(GrammarError):
        assert g.parse(l.lex("a * b * c")) == '(a * (b * c))'


def test_non_assoc_higher():
    l = make_l()  # noqa

    def assoc(g):
        g.nonassoc('+')
        g.nonassoc('*')

    g = make_g(assoc=assoc)

    with pytest.raises(GrammarError):
        assert g.parse(l.lex("a + b + c")) == '(a + b + c)'

    assert g.parse(l.lex("a * b + c")) == '((a * b) + c)'
    assert g.parse(l.lex("a + b * c")) == '(a + (b * c))'

    with pytest.raises(GrammarError):
        assert g.parse(l.lex("a * b * c")) == '(a * b * c)'


def test_non_assoc_lower():
    l = make_l()  # noqa

    def assoc(g):
        g.nonassoc('*')
        g.nonassoc('+')

    g = make_g(assoc=assoc)

    with pytest.raises(GrammarError):
        assert g.parse(l.lex("a + b + c")) == '(a + b + c)'

    assert g.parse(l.lex("a * b + c")) == '(a * (b + c))'
    assert g.parse(l.lex("a + b * c")) == '((a + b) * c)'

    with pytest.raises(GrammarError):
        assert g.parse(l.lex("a * b * c")) == '(a * b * c)'


def test_right_equal():
    l = make_l()

    def assoc(g):
        g.right('+', '*')

    g = make_g(assoc=assoc)

    assert g.parse(l.lex("a + b + c")) == '(a + (b + c))'
    assert g.parse(l.lex("a * b + c")) == '(a * (b + c))'
    assert g.parse(l.lex("a + b * c")) == '(a + (b * c))'
    assert g.parse(l.lex("a * b * c")) == '(a * (b * c))'


def test_left_equal():
    l = make_l()

    def assoc(g):
        g.left('+', '*')

    g = make_g(assoc=assoc)

    assert g.parse(l.lex("a + b + c")) == '((a + b) + c)'
    assert g.parse(l.lex("a * b + c")) == '((a * b) + c)'
    assert g.parse(l.lex("a + b * c")) == '((a + b) * c)'
    assert g.parse(l.lex("a * b * c")) == '((a * b) * c)'


def test_right_higher():
    l = make_l()

    def assoc(g):
        g.left('+')
        g.right('*')

    g = make_g(assoc=assoc)

    assert g.parse(l.lex("a + b + c")) == '((a + b) + c)'
    assert g.parse(l.lex("a * b + c")) == '((a * b) + c)'
    assert g.parse(l.lex("a + b * c")) == '(a + (b * c))'
    assert g.parse(l.lex("a * b * c")) == '(a * (b * c))'


def test_left_higher():
    l = make_l()

    def assoc(g):
        g.left('+')
        g.left('*')

    g = make_g(assoc=assoc)

    assert g.parse(l.lex("a + b + c")) == '((a + b) + c)'
    assert g.parse(l.lex("a * b + c")) == '((a * b) + c)'
    assert g.parse(l.lex("a + b * c")) == '(a + (b * c))'
    assert g.parse(l.lex("a * b * c")) == '((a * b) * c)'


def test_right_lower():
    l = make_l()

    def assoc(g):
        g.right('*')
        g.left('+')

    g = make_g(assoc=assoc)

    assert g.parse(l.lex("a + b + c")) == '((a + b) + c)'
    assert g.parse(l.lex("a * b + c")) == '(a * (b + c))'
    assert g.parse(l.lex("a + b * c")) == '((a + b) * c)'
    assert g.parse(l.lex("a * b * c")) == '(a * (b * c))'


def test_left_lower():
    l = make_l()

    def assoc(g):
        g.left('*')
        g.left('+')

    g = make_g(assoc=assoc)

    assert g.parse(l.lex("a + b + c")) == '((a + b) + c)'
    assert g.parse(l.lex("a * b + c")) == '(a * (b + c))'
    assert g.parse(l.lex("a + b * c")) == '((a + b) * c)'
    assert g.parse(l.lex("a * b * c")) == '((a * b) * c)'
