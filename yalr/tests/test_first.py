from .. import SLR, Production
from .g_4_11 import make_g


def test_first():
    g = make_g(SLR, compile=False)
    n = g.nt

    E = n.E
    E_ = n.E_
    T = n.T
    T_ = n.T_
    F = n.F

    assert g._first(E) == g._first(T) == g._first(F) == {'(', str}
    assert g._first(E_) == {'+', Production.Empty}
    assert g._first(T_) == {'*', Production.Empty}

    assert g.first([E, T, F]) == {'(', str}
    assert g.first([E_, T_]) == {'+', '*', Production.Empty}
