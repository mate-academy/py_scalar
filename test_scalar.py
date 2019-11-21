"""
docstring
"""
import scalar


def test_scalar():
    """

    :return:
    """
    assert scalar.scalar_product([1, 2, 3], [1, 2, 3]) == 14


def test_empty():
    """

    :return:
    """
    assert scalar.scalar_product([], []) == 0


def test_different():
    """

    :return:
    """
    assert scalar.scalar_product([1, 1], [1, 1, 1]) == 2
