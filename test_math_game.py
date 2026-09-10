from math_game import Polynomial

def test_evaluate_polynomial_quadratic():
    """f(x) = x^2 + 2x + 1, evaluated at x=3 should give 16"""
    poly = Polynomial.set_polynomial(1, 2, 1, 0, 0, 0)
    result = Polynomial.evaluate_polynomial(poly, 3)
    assert result == 16
    

def test_evaluate_polynomial_constant():
    """f(x) = 5 (no x terms), should equal 5 for any x"""
    poly = Polynomial.set_polynomial(5, 0, 0, 0, 0, 0)
    result = Polynomial.evaluate_polynomial(poly, 100)
    assert result == 5


def test_evaluate_polynomial_at_zero():
    """f(x) = x^2 + 2x + 1, evaluated at x=0 should just give the constant term"""
    poly = Polynomial.set_polynomial(1, 2, 1, 0, 0, 0)
    result = Polynomial.evaluate_polynomial(poly, 0)
    assert result == 1


def test_evaluate_polynomial_negative_x():
    """f(x) = x^2 + 2x + 1, evaluated at x=-3: 9 - 6 + 1 = 4"""
    poly = Polynomial.set_polynomial(1, 2, 1, 0, 0, 0)
    result = Polynomial.evaluate_polynomial(poly, -3)
    assert result == 4


def test_evaluate_polynomial_negative_coefficients():
    """f(x) = -x^2 + 3, evaluated at x=2: -4 + 3 = -1"""
    poly = Polynomial.set_polynomial(3, 0, -1, 0, 0, 0)
    result = Polynomial.evaluate_polynomial(poly, 2)
    assert result == -1