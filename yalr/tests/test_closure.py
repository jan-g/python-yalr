from .. import SLR, Production
from .g_4_19 import make_g


def test_productions():
    g = make_g(SLR)
    assert len(g.productions()) == 7

    ps = g.productions(g.nt.E_)
    assert len(ps) == 1
    p = ps.pop()
    assert isinstance(p, Production)


def test_closure():
    g = make_g(SLR)

    ps = g.nt.E_.productions
    assert len(ps) == 1
    p = ps.pop()

    i = {(0, p)}
    cl = g._closure(i)

    assert len(i) == 1
    assert cl == {
        (0, p) for p in g.productions()
    }
