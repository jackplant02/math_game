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