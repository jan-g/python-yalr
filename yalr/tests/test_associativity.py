import pytest

from .. import LR1, Lexer, GrammarError


def make_l():
    l = Lexer()

    @l('\s+')
    def whitespace():
        pass

    @l('( [+*^] )')
    def plus(op):
        return op

    @l(r'(?P<token> [a-zA-Z_]\w* )')
    def ident(token=None):
        return token

    return l


def make_g(Grammar=LR1, compile=True, assoc=None, **kwargs):
    g = Grammar()
    if assoc is not None:
        assoc(g)
    n = g.nt

    @n.E(str)
    def _(id):
        return id

    @n.E(n.E, '+', n.E, **kwargs)
    def plus(e1, _, e2):
        return "({} + {})".format(e1, e2)

    if compile:
        g.compile(start=n.E)

    return g


def test_non_assoc():
    l = make_l()

    def assoc(g):
        g.nonassoc('+')

    g = make_g(assoc=assoc)

    with pytest.raises(GrammarError):
        assert g.parse(l.lex("a + b + c")) == '(a + b + c)'


def test_left_assoc():
    l = make_l()

    def assoc(g):
        g.left('+')

    g = make_g(assoc=assoc, prec='+')

    assert g.parse(l.lex("a + b + c")) == '((a + b) + c)'


def test_right_assoc():
    l = make_l()

    def assoc(g):
        g.right('+')

    g = make_g(assoc=assoc, prec='+')

    assert g.parse(l.lex("a + b + c")) == '(a + (b + c))'
