from .. import LR1, Lexer
from .debug import write_tables
from .g_4_21 import make_g


def test_closure():
    g = make_g(LR1, compile=False)
    S_ = g.nt.S_
    S = g.nt.S
    C = g.nt.C

    I0 = g._closure({(0, S_[S], Lexer.EOF)})
    assert I0 == {
        (0, S_[S], Lexer.EOF),
        (0, S[C, C], Lexer.EOF),
        (0, C['c', C], 'c'),
        (0, C['c', C], 'd'),
        (0, C['d'], 'c'),
        (0, C['d'], 'd'),
    }

    I1 = g._goto(I0, S)
    assert I1 == {
        (1, S_[S], Lexer.EOF),
    }


def fs(*args):
    return frozenset(args)


def test_sets_of_items():
    g = make_g(LR1, compile=False)
    S_ = g.nt.S_
    S = g.nt.S
    C = g.nt.C

    items = g._sets_of_items(S_[S])

    assert items == {
        fs(  # I0
            (0, S_[S], Lexer.EOF),
            (0, S[C, C], Lexer.EOF),
            (0, C['c', C], 'c'), (0, C['c', C], 'd'),
            (0, C['d'], 'c'), (0, C['d'], 'd'),
        ),
        fs(  # I1
            (1, S_[S], Lexer.EOF),
        ),
        fs(  # I2
            (1, S[C, C], Lexer.EOF),
            (0, C['c', C], Lexer.EOF),
            (0, C['d'], Lexer.EOF),
        ),
        fs(  # I3
            (1, C['c', C], 'c'), (1, C['c', C], 'd'),
            (0, C['c', C], 'c'), (0, C['c', C], 'd'),
            (0, C['d'], 'c'), (0, C['d'], 'd'),
        ),
        fs(  # I4
            (1, C['d'], 'c'), (1, C['d'], 'd'),
        ),
        fs(  # I5
            (2, S[C, C], Lexer.EOF),
        ),
        fs(  # I6
            (1, C['c', C], Lexer.EOF),
            (0, C['c', C], Lexer.EOF),
            (0, C['d'], Lexer.EOF),
        ),
        fs(  # I7
            (1, C['d'], Lexer.EOF),
        ),
        fs(  # I8
            (2, C['c', C], 'c'), (2, C['c', C], 'd'),
        ),
        fs(  # I9
            (2, C['c', C], Lexer.EOF),
        ),
    }


def test_tables():
    g = make_g(LR1)
    write_tables(g)
