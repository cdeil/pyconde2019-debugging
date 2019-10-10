def product(a, b):
    result = a ** b
    return result


def test_product():
    a, b = 2, 3

    result = product(a, b)

    assert result == 6
