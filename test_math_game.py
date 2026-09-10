import random
import builtins
from math_game import Polynomial, Questions

# question 1
def test_question1_correct(monkeypatch):
    """
    Question 1 should return True if the question is -79 + 46
    and the user inputs -33.
    """
    random_values = iter([-79, 46])
    monkeypatch.setattr(random, "randint", lambda a, b: next(random_values))
    monkeypatch.setattr(builtins, "input", lambda prompt="": "-33")

    result = Questions.question1()

    assert result == True

def test_question1_incorrect(monkeypatch):
    """
    Question 1 should return False if the question is -79 + 46
    and the user inputs -100.
    """
    random_values = iter([-79, 46])
    monkeypatch.setattr(random, "randint", lambda a, b: next(random_values))
    monkeypatch.setattr(builtins, "input", lambda prompt="": "-100")

    result = Questions.question1()

    assert result == False

def test_question1_bad(monkeypatch):
    """
    Question 1 should return False if the question is -79 + 46
    and the user inputs text.
    """
    random_values = iter([-79, 46])
    monkeypatch.setattr(random, "randint", lambda a, b: next(random_values))
    monkeypatch.setattr(builtins, "input", lambda prompt="": "text")

    result = Questions.question1()

    assert result == False

def test_question1_blank(monkeypatch):
    """
    Question 1 should return False if the question is -79 + 46
    and the user inputs nothing.
    """
    random_values = iter([-79, 46])
    monkeypatch.setattr(random, "randint", lambda a, b: next(random_values))
    monkeypatch.setattr(builtins, "input", lambda prompt="": "")

    result = Questions.question1()

    assert result == False

# question 2
def test_question2_correct(monkeypatch):
    """
    Question 2 should return True if the question is -5 + 6
    and the user inputs -30.
    """
    random_values = iter([-5, 6])
    monkeypatch.setattr(random, "randint", lambda a, b: next(random_values))
    monkeypatch.setattr(builtins, "input", lambda prompt="": "-30")

    result = Questions.question2()

    assert result == True

def test_question2_incorrect(monkeypatch):
    """
    Question 1 should return False if the question is -5 + 6
    and the user inputs 2.
    """
    random_values = iter([-5, 6])
    monkeypatch.setattr(random, "randint", lambda a, b: next(random_values))
    monkeypatch.setattr(builtins, "input", lambda prompt="": "2")

    result = Questions.question2()

    assert result == False

def test_question2_bad(monkeypatch):
    """
    Question 1 should return False if the question is -5 + 6
    and the user inputs text.
    """
    random_values = iter([-5, 6])
    monkeypatch.setattr(random, "randint", lambda a, b: next(random_values))
    monkeypatch.setattr(builtins, "input", lambda prompt="": "text")

    result = Questions.question2()

    assert result == False

def test_question2_blank(monkeypatch):
    """
    Question 1 should return False if the question is -5 + 6
    and the user inputs nothing.
    """
    random_values = iter([-5, 6])
    monkeypatch.setattr(random, "randint", lambda a, b: next(random_values))
    monkeypatch.setattr(builtins, "input", lambda prompt="": "")

    result = Questions.question2()

    assert result == False

# question 3
def test_question3_no_sol_correct(monkeypatch):
    """
    Question 3 should return True if the equation is x^2 + 5 = 0
    and the user inputs n/a.
    """
    random_values = iter([1, 0, 5])
    monkeypatch.setattr(random, "randint", lambda a, b: next(random_values))
    monkeypatch.setattr(builtins, "input", lambda prompt="": "n/a")

    result = Questions.question3()

    assert result == True

def test_question3_no_sol_incorrect(monkeypatch):
    """
    Question 3 should return False if the equation is x^2 + 5 = 0
    and the user inputs 2.
    """
    random_values = iter([1, 0, 5])
    monkeypatch.setattr(random, "randint", lambda a, b: next(random_values))
    monkeypatch.setattr(builtins, "input", lambda prompt="": "2")

    result = Questions.question3()

    assert result == False

def test_question3_one_sol_correct(monkeypatch):
    """
    Question 3 should return True if the equation is x^2 -4x + 4 = 0
    and the user inputs 2.
    """
    random_values = iter([1, -4, 4])
    monkeypatch.setattr(random, "randint", lambda a, b: next(random_values))
    monkeypatch.setattr(builtins, "input", lambda prompt="": "2")

    result = Questions.question3()

    assert result == True

def test_question3_one_sol_incorrect(monkeypatch):
    """
    Question 3 should return False if the equation is x^2 -4x + 4 = 0
    and the user inputs 3.
    """
    random_values = iter([1, -4, 4])
    monkeypatch.setattr(random, "randint", lambda a, b: next(random_values))
    monkeypatch.setattr(builtins, "input", lambda prompt="": "3")

    result = Questions.question3()

    assert result == False

def test_question3_two_sol_correct(monkeypatch):
    """
    Question 3 should return True if the equation is x^2 -3x - 1 = 0
    and the user inputs 3.303 and -0.303.
    """
    random_values = iter([1, -3, -1])
    answers = iter(["3.303", "-0.303"])
    monkeypatch.setattr(random, "randint", lambda a, b: next(random_values))
    monkeypatch.setattr(builtins, "input", lambda prompt="": next(answers))

    result = Questions.question3()

    assert result == True

def test_question3_two_sol_incorrect(monkeypatch):
    """
    Question 3 should return False if the equation is x^2 -3x - 1 = 0
    and the user inputs 5 and 2.
    """
    random_values = iter([1, -3, -1])
    answers = iter(["5", "2"])
    monkeypatch.setattr(random, "randint", lambda a, b: next(random_values))
    monkeypatch.setattr(builtins, "input", lambda prompt="": next(answers))

    result = Questions.question3()

    assert result == False

def test_question3_bad(monkeypatch):
    """
    Question 3 should return False if the equation is x^2 -3x - 1 = 0
    and the user inputs text.
    """
    random_values = iter([1, -3, -1])
    monkeypatch.setattr(random, "randint", lambda a, b: next(random_values))
    monkeypatch.setattr(builtins, "input", lambda prompt="": "text")

    result = Questions.question3()

    assert result == False

# question 4
def test_question4_correct(monkeypatch):
    """
    Question 4 should return True if the given polynomial is x^4 + x^3 - x^2 + 4x + 4,
    x = 19, and the user inputs -26311.
    """
    random_values = iter([0, 1, 1, -1, 4, 4, -19])
    monkeypatch.setattr(random, "randint", lambda a, b: next(random_values))
    monkeypatch.setattr(builtins, "input", lambda prompt="": "-26311")

    result = Questions.question4()

    assert result == True

def test_question4_incorrect(monkeypatch):
    """
    Question 4 should return False if the given polynomial is x^4 + x^3 - x^2 + 4x + 4,
    x = 19, and the user inputs -2.
    """
    random_values = iter([0, 1, 1, -1, 4, 4, -19])
    monkeypatch.setattr(random, "randint", lambda a, b: next(random_values))
    monkeypatch.setattr(builtins, "input", lambda prompt="": "-2")

    result = Questions.question4()

    assert result == False

def test_question4_bad(monkeypatch):
    """
    Question 4 should return False if the given polynomial is x^4 + x^3 - x^2 + 4x + 4,
    x = 19, and the user inputs text.
    """
    random_values = iter([0, 1, 1, -1, 4, 4, -19])
    monkeypatch.setattr(random, "randint", lambda a, b: next(random_values))
    monkeypatch.setattr(builtins, "input", lambda prompt="": "text")

    result = Questions.question4()

    assert result == False

# question 4
def test_question5_correct(monkeypatch):
    """
    Question 5 should return True if the given vectors are <2, 3, 1, 5> and
    <-4, 3, 0, -5>, and the user inputs -24.
    """
    random_values = iter([4, 2, -4, 3, 3, 1, 0, 5, -5])
    monkeypatch.setattr(random, "randint", lambda a, b: next(random_values))
    monkeypatch.setattr(builtins, "input", lambda prompt="": "-24")

    result = Questions.question5()

    assert result == True

def test_question5_incorrect(monkeypatch):
    """
    Question 5 should return False if the given vectors are <2, 3, 1, 5> and
    <-4, 3, 0, -5>, and the user inputs -2.
    """
    random_values = iter([4, 2, -4, 3, 3, 1, 0, 5, -5])
    monkeypatch.setattr(random, "randint", lambda a, b: next(random_values))
    monkeypatch.setattr(builtins, "input", lambda prompt="": "-2")

    result = Questions.question5()

    assert result == False

def test_question5_bad(monkeypatch):
    """
    Question 5 should return False if the given vectors are <2, 3, 1, 5> and
    <-4, 3, 0, -5>, and the user inputs text.
    """
    random_values = iter([4, 2, -4, 3, 3, 1, 0, 5, -5])
    monkeypatch.setattr(random, "randint", lambda a, b: next(random_values))
    monkeypatch.setattr(builtins, "input", lambda prompt="": "text")

    result = Questions.question5()

    assert result == False

# question 6

# correct answer, 2 intercepts
def test_question6_two_intercepts_correct(monkeypatch):
    """
    Question 6 should return True if the given curves are 2x^2 + 5x - 3 and
    x^2 + 2x + 1 and the user inputs 20.833.
    """
    random_values = iter([2, 5, -3, 1, 2, 1])
    monkeypatch.setattr(random, "randint", lambda a, b: next(random_values))
    monkeypatch.setattr(builtins, "input", lambda prompt="": "20.833")

    result = Questions.question6()

    assert result == True

# incorrect answer, 2 intercepts
def test_question6_two_intercepts_incorrect(monkeypatch):
    """
    Question 6 should return False if the given curves are 2x^2 + 5x - 3 and
    x^2 + 2x + 1 and the user inputs 2.
    """
    random_values = iter([2, 5, -3, 1, 2, 1])
    monkeypatch.setattr(random, "randint", lambda a, b: next(random_values))
    monkeypatch.setattr(builtins, "input", lambda prompt="": "2")

    result = Questions.question6()

    assert result == False

# bad answer, 2 intercept
def test_question6_two_intercepts_bad(monkeypatch):
    """
    Question 6 should return False if the given curves are 2x^2 + 5x - 3 and
    x^2 + 2x + 1 and the user inputs text.
    """
    random_values = iter([2, 5, -3, 1, 2, 1])
    monkeypatch.setattr(random, "randint", lambda a, b: next(random_values))
    monkeypatch.setattr(builtins, "input", lambda prompt="": "text")

    result = Questions.question6()

    assert result == False

# correct answer, 1 intercept
def test_question6_one_intercept_correct(monkeypatch):
    """
    Question 6 should return True if the given curves are x^2 and
    -x^2 and the user inputs 0.
    """
    random_values = iter([1, 0, 0, -1, 0, 0])
    monkeypatch.setattr(random, "randint", lambda a, b: next(random_values))
    monkeypatch.setattr(builtins, "input", lambda prompt="": "0")

    result = Questions.question6()

    assert result == True

# incorrect answer, 1 intercept
def test_question6_one_intercept_incorrect(monkeypatch):
    """
    Question 6 should return False if the given curves are x^2 and
    -x^2 and the user inputs 1.
    """
    random_values = iter([1, 0, 0, -1, 0, 0])
    monkeypatch.setattr(random, "randint", lambda a, b: next(random_values))
    monkeypatch.setattr(builtins, "input", lambda prompt="": "1")

    result = Questions.question6()

    assert result == False

# bad answer, 1 intercept
def test_question6_one_intercept_bad(monkeypatch):
    """
    Question 6 should return False if the given curves are x^2 + 1 and
    -x^2 + 1 and the user inputs text.
    """
    random_values = iter([1, 0, 1, -1, 0, 1])
    monkeypatch.setattr(random, "randint", lambda a, b: next(random_values))
    monkeypatch.setattr(builtins, "input", lambda prompt="": "text")

    result = Questions.question6()

    assert result == False

# correct answer, no intercepts
def test_question6_no_intercept_correct(monkeypatch):
    """
    Question 6 should return True if the given curves are x^2 and
    -x^2 - 1 and the user inputs 0.
    """
    random_values = iter([1, 0, 0, -1, 0, -1])
    monkeypatch.setattr(random, "randint", lambda a, b: next(random_values))
    monkeypatch.setattr(builtins, "input", lambda prompt="": "0")

    result = Questions.question6()

    assert result == True

# incorrect answer, no intercepts
def test_question6_no_intercept_incorrect(monkeypatch):
    """
    Question 6 should return False if the given curves are x^2 and
    -x^2 - 1 and the user inputs 25.
    """
    random_values = iter([1, 0, 0, -1, 0, -1])
    monkeypatch.setattr(random, "randint", lambda a, b: next(random_values))
    monkeypatch.setattr(builtins, "input", lambda prompt="": "25")

    result = Questions.question6()

    assert result == False

# bad answer, no intercepts
def test_question6_no_intercept_bad(monkeypatch):
    """
    Question 6 should return False if the given curves are x^2 and
    -x^2 - 1 and the user inputs text.
    """
    random_values = iter([1, 0, 0, -1, 0, -1])
    monkeypatch.setattr(random, "randint", lambda a, b: next(random_values))
    monkeypatch.setattr(builtins, "input", lambda prompt="": "text")

    result = Questions.question6()

    assert result == False

# question 7
def test_question_7_full_equation_correct(monkeypatch):
    """
    For the following version of Question 7, the function should return 
    True if the user inputs 4.

    Question:
        Consider the function f(x, y) = 2xe^y + cos(x) + sin(x) + 3xy + y^2 + y + x^2 + 2x + 1
        Compute the directional derivative of f(x, y) at the point (0, 0)
        in the direction opposite to the vector <-3, -4>.
    """
    random_values = iter([2, 1, 1, 1, 1, 1, 3, 1, 2, 1, 1, 1, 3, 4, 0, 0])
    monkeypatch.setattr(random, "randint", lambda a, b: next(random_values))
    monkeypatch.setattr(builtins, "input", lambda prompt="": "4")

    result = Questions.question7()

    assert result == True

def test_question_7_full_equation_incorrect(monkeypatch):
    """
    For the following version of Question 7, the function should return 
    False if the user inputs 4.001.

    Question:
        Consider the function f(x, y) = 2xe^y + cos(x) + sin(x) + 3xy + y^2 + y + x^2 + 2x + 1
        Compute the directional derivative of f(x, y) at the point (0, 0)
        in the direction opposite to the vector <-3, -4>.
    """
    random_values = iter([2, 1, 1, 1, 1, 1, 3, 1, 2, 1, 1, 1, 3, 4, 0, 0])
    monkeypatch.setattr(random, "randint", lambda a, b: next(random_values))
    monkeypatch.setattr(builtins, "input", lambda prompt="": "4.001")

    result = Questions.question7()

    assert result == False

def test_question_7_full_equation_bad(monkeypatch):
    """
    For the following version of Question 7, the function should return 
    False if the user inputs text.

    Question:
        Consider the function f(x, y) = 2xe^y + cos(x) + sin(x) + 3xy + y^2 + y + x^2 + 2x + 1
        Compute the directional derivative of f(x, y) at the point (0, 0)
        in the direction opposite to the vector <-3, -4>.
    """
    random_values = iter([2, 1, 1, 1, 1, 1, 3, 1, 2, 1, 1, 1, 3, 4, 0, 0])
    monkeypatch.setattr(random, "randint", lambda a, b: next(random_values))
    monkeypatch.setattr(builtins, "input", lambda prompt="": "text")

    result = Questions.question7()

    assert result == False

def test_question_7_poly_only_correct(monkeypatch):
    """
    For the following version of Question 7, the function should return 
    True if the user inputs 2.

    Question:
        Consider the function f(x, y) = 2y + x + 2
        Compute the directional derivative of f(x, y) at the point (2, 3)
        in the direction opposite to the vector <0, -5>.
    """
    random_values = iter([0, 2, 0, 0, 2, 2, 0, 2, 1, 2, 0, 0, 0, 5, 2, 3])
    monkeypatch.setattr(random, "randint", lambda a, b: next(random_values))
    monkeypatch.setattr(builtins, "input", lambda prompt="": "2")

    result = Questions.question7()

    assert result == True

