from .. import SLR
from .debug import write_tables
from .g_4_19 import make_g


def test_tables():
    g = make_g(SLR)
    write_tables(g)
