import scalar


def test_scalar():
    assert scalar.scalar_product_den_solution([1, 2, 3], [1, 2, 3]) == 14


def test_empty():
    assert scalar.scalar_product_den_solution([], []) == 0


def test_different():
    assert scalar.scalar_product_den_solution([1, 1], [1, 1, 1]) == 2