import pytest

from .. import SLR, Production
from .g_4_19 import make_g


def test_find_productions():
    g = make_g(SLR)
    n = g.nt

    E_ = n.E_
    E = n.E

    assert isinstance(E_[E], Production)
    with pytest.raises(KeyError):
        assert isinstance(E_[E, '+'], Production)


def test_goto():
    g = make_g(SLR)
    n = g.nt

    E_ = n.E_
    E = n.E
    T = n.T
    F = n.F

    i = set()
    i.add((1, E_[E]))
    i.add((1, E[E, '+', T]))

    goto = g._goto(i, '+')

    assert goto == {
        (2, E[E, '+', T]),
        (0, T[T, '*', F]),
        (0, T[F]),
        (0, F['(', E, ')']),
        (0, F[str]),
    }

    for n, p in goto:
        print n, p
