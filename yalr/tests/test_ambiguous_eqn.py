import pytest

from .. import LR1, GrammarError
from .l_tokens import make_l
from .g_4_25 import make_g


def test_eqn():
    l = make_l()
    g = make_g(LR1)

    assert g.parse(l.lex("x")) == 'x'
    assert g.parse(l.lex("{x}")) == 'x'

    assert g.parse(l.lex("x sub x")) == '(x sub x)'
    assert g.parse(l.lex("x sup x")) == '(x sup x)'

    assert g.parse(l.lex("x sub {x sup x}")) == '(x sub (x sup x))'
    assert g.parse(l.lex("{x sub x} sup x")) == '((x sub x) sup x)'

    assert g.parse(l.lex("x sub x sup x")) == '(x sub x sup x)'


def test_eqn_errors():
    l = make_l()
    g = make_g(LR1)

    with pytest.raises(GrammarError):
        assert g.parse(l.lex("{x")) is None

    with pytest.raises(GrammarError):
        assert g.parse(l.lex("x x")) is None

    with pytest.raises(GrammarError):
        assert g.parse(l.lex("x { x }")) is None
