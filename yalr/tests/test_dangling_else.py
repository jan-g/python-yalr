""" Dangling else resolution

    This should be resolvable with a default
    shift/reduce strategy of "prefer to shift".
"""

from .. import LR1
from .l_words import make_l


def make_g(Grammar=LR1, compile=True, assoc=None):
    g = Grammar()
    if assoc is not None:
        assoc(g)
    n = g.nt

    @n.S('if', n.S, 'then', n.S, 'else', n.S)
    def _(_if, s1, _then, s2, _else, s3):
        return "(if {} then {} else {})".format(s1, s2, s3)

    @n.S('if', n.S, 'then', n.S)  # noqa
    def _(_if, s1, _then, s2):
        return "(if {} then {})".format(s1, s2)

    @n.S(str)  # noqa
    def _(s):
        return s

    if compile:
        g.compile(start=n.S)

    return g


def test_compiles():
    l = make_l()
    g = make_g()

    assert g.parse(l.lex("if a then b")) == '(if a then b)'

    assert g.parse(l.lex("if a then b else c")) == '(if a then b else c)'

    assert g.parse(l.lex("if a then b else if c then d")) == \
        '(if a then b else (if c then d))'

    assert g.parse(l.lex("if a then if b then c else d")) == \
        '(if a then (if b then c else d))'

    assert g.parse(l.lex("if a then if b then c else d else e")) == \
        '(if a then (if b then c else d) else e)'

    assert len(g._shift_reduce_conflicts) > 0
