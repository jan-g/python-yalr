from .. import LR


def test_equality():
    assert LR.Shift(1) == LR.Shift(1)
    assert not(LR.Shift(1) != LR.Shift(1))
    assert LR.Shift(2) != LR.Shift(1)
    assert LR.Shift(1) != LR.Reduce("rule")
    assert LR.Shift(1) != LR.Accept()
    assert LR.Shift(1) != LR.Error()

    assert LR.Reduce("foo") == LR.Reduce("foo")
    assert not(LR.Reduce("foo") != LR.Reduce("foo"))
    assert LR.Reduce("foo") != LR.Reduce("bar")
    assert LR.Reduce("foo") != LR.Shift(1)
    assert LR.Reduce("foo") != LR.Accept()
    assert LR.Reduce("foo") != LR.Error()

    assert LR.Accept() == LR.Accept()
    assert not(LR.Accept() != LR.Accept())
    assert LR.Accept() != LR.Reduce("foo")
    assert LR.Accept() != LR.Shift(1)
    assert LR.Accept() != LR.Error()

    assert LR.Error() != LR.Shift(1)
    assert LR.Error() != LR.Reduce("foo")
    assert LR.Error() != LR.Accept()
