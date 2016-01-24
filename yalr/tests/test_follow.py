from .. import SLR, Lexer
from .g_4_11 import make_g


def test_follow():
    g = make_g(SLR, compile=False)
    n = g.nt

    E = n.E
    E_ = n.E_
    T = n.T
    T_ = n.T_
    F = n.F

    # the start symbol is usually assigned by .compile
    # instead, it'll be cached by the .follow computation.
    assert g.follow(E, start=E) == g.follow(E_) == {')', Lexer.EOF}
    assert g.follow(T) == g.follow(T_) == {'+', ')', Lexer.EOF}
    assert g.follow(F) == {'+', '*', ')', Lexer.EOF}
