import pytest

from .. import SLR, LR1, GrammarError
from .g_4_20 import make_g


def test_tables():
    with pytest.raises(GrammarError):
        g = make_g(SLR)  # noqa


def test_lr1():
    g = make_g(LR1)  # noqa
