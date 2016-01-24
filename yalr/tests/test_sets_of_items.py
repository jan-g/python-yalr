from .. import SLR
from .g_4_19 import make_g


def test_terminals():
    g = make_g(SLR)
    t = g.terminals

    assert t == {
        '+', '*', '(', ')', str,
    }


def test_symbols():
    g = make_g(SLR)
    n = g.nt

    E_ = n.E_
    E = n.E
    T = n.T
    F = n.F

    assert g.symbols == {
        '+', '*', '(', ')', str,
        E_, E, T, F,
    }


def test_sets_of_items():
    g = make_g(SLR)
    n = g.nt

    E_ = n.E_
    E = n.E

    c = g._sets_of_items(E_[E])

    assert sorted(len(s) for s in c) == [1, 1, 1, 1, 2, 2, 2, 2, 3, 5, 7, 7]
