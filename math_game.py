import random
import cmath
import math

# Initialize score and done bools

global score
score = 0
global done
done = [False] * 8

class Polynomial:
    coefficient_list = []

    @staticmethod
    def set_polynomial(pow0, pow1, pow2, pow3, pow4, pow5):
        Polynomial.coefficient_list.clear()
        Polynomial.coefficient_list.extend([pow5, pow4, pow3, pow2, pow1, pow0])
        return True

    def get_polynomial(self):
        """
        Returns the polynomial in the form of a string
        """
        polynomial_set = []
        zeros_count = 0

        for i in range(len(Polynomial.coefficient_list)):
            if Polynomial.coefficient_list[i] == 0:
                zeros_count += 1
                if i == len(Polynomial.coefficient_list) - 1 and len(polynomial_set) >= 3:
                    del polynomial_set[len(polynomial_set) - 3:]

            elif i < len(Polynomial.coefficient_list) - 1:

                if len(Polynomial.coefficient_list) - i - 1 == 1:
                    if Polynomial.coefficient_list[i] == 1:
                        polynomial_set.append(f"x + ")
                    elif Polynomial.coefficient_list[i] == -1:
                        polynomial_set.append(f"-x + ")
                    else:
                        polynomial_set.append(f"{Polynomial.coefficient_list[i]}x + ")

                else:
                    if Polynomial.coefficient_list[i] == 1:
                        polynomial_set.append(f"x^{len(Polynomial.coefficient_list) - i - 1} + ")
                    elif Polynomial.coefficient_list[i] == -1:
                        polynomial_set.append(f"-x^{len(Polynomial.coefficient_list) - i - 1} + ")
                    else:
                        polynomial_set.append(f"{Polynomial.coefficient_list[i]}x^{len(Polynomial.coefficient_list) - i - 1} + ")

            else:
                polynomial_set.append(f"{Polynomial.coefficient_list[i]}")

            if zeros_count == len(Polynomial.coefficient_list):
                return "0"

        result = ""
        for item in polynomial_set:
            result += item

        result = result.replace("+ -", "- ")
        return result

    def evaluate_polynomial(self, x):
        """
        Evaluates this polynomial at the x passed to the method.
        :param x: The x value to evaluate the polynomial at.
        """
        sum = 0
        
        for i in range(len(self.coefficient_list)):
            sum += self.coefficient_list[i] * (x ** (len(self.coefficient_list) - i - 1))

        return sum

    def evaluate_polynomial_derivative(self, x):
        """
        Evaluates the 1st derivative of this polynomial at x. This uses the
        exact numerical technique, since it is easy to obtain the derivative of a 
        polynomial.
        """

        sum = 0

        for i in range(len(self.coefficient_list)):
            if x == 0 and len(self.coefficient_list) - i - 2 < 0:
                term = 0
            else:
                term = (len(self.coefficient_list) - i - 1) * self.coefficient_list[i] * (x ** (len(self.self.coefficient_list) - i - 2))
            sum += term

        return sum


    def evaluate_polynomial_integral(self, a, b):

        sum = 0

        for i in range(len(self.coefficient_list)):
            term1 = self.coefficient_list[i] / (len(self.coefficient_list) - i - 1) * (a ** len(self.coefficient_list) - i)
            term2 = self.coefficient_list[i] / (len(self.coefficient_list) - i - 1) * (b ** len(self.coefficient_list) - i)
            term = term1 + term2
            sum += term

        return sum

class Matrix:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def find_lambda(self):
        values = [complex(0,0)] * 2
        c1 = 1
        c2 = -self.a - self.d
        c3 = self.a * self.d - self.b * self.c
        D = c2 * c2 - 4 * c1 * c3

        values[0] = (-c2 + cmath.sqrt(D)) / 2
        values[1] = (-c2 - cmath.sqrt(D)) / 2
        return values

    def find_real_eigenvector(self, lambda_val):
        l = lambda_val.real
        v = [0.0, 0.0]

        if self.b == 0 and self.a != 1:
            v[1] = 1
            v[0] = 0

        elif self.a != l and self.b != 0:
            v[1] = 1
            v[0] = -self.b / (self.a - l)

        elif(self.a == l and self.b != 0):
            v[0] = 1
            v[1] = 0

        else:
            if self.d != l and self.c != 0:
                v[1] = 1
                v[0] = (l - d) / case
            elif self.d == l and self.c != 0:
                v[1] = 1
                v[0] = 0
            elif self.c == 0 and d != l:
                v[0] = 1
                v[1] = 0
            else:
                v[0] = 1
                v[1] = 2
        return v

    def find_complex_eigenvector(self, lamda_val):
       v = [complex(0, 0)] * 2
       v[1] = complex(1, 0)
       v[0] = -self.b / (self.a - lamda_val)
       return v

    def find_generalized_eigenvector(self, lambda_val, v):
        l = lambda_val.real
        u = [0.0, 0.0]

        if self.b == 0 and self.a != l:
            u[1] = 1
            u[0] = v[0] / (self.a - l)

        elif self.a != l and self.b != 0:
            u[1] = 1
            u[0] = (v[0] - self.b) / (self.a - l)

        elif self.a == l and self.b != 0:
            u[0] = 1
            u[1] = v[0] / self.b

        else:
            if self.d != l and self.c != 0:
                u[1] = 1
                u[0] = (v[1] + l - self.d) / self.c
            elif self.d == l and self.c != 0:
                u[1] = 1
                u[0] = v[1] / self.c

            elif self.c == 0 and self.d != 1:
                u[0] = 1
                u[1] = v[1] / (self.d - 1)
            else:
                u[0] = 3
                u[1] = 1

        return u
            
    
class Questions:
    @staticmethod
    def question_text(q, done_index):
        global done
        global score
        if done[done_index]:
            print("\nYou have already answered this question correctly.")
        else:
            if q():
                score += 1
                done[done_index] = True
                print("\nCorrect!")
                print(f"Current score: {score}/8")

            else:
                print("\nIncorrect answer.")
                print(f"Current score: {score}/8")

    def question1():
        num1 = random.randint(-100, 100)
        num2 = random.randint(-100, 100)

        if num2 < 0:
            answer = input(f"\n{num1} - {-1 * num2} = ").strip()
        else:
            answer = input(f"\n{num1} + {num2} = ").strip()

        if answer == "":
            return False

        try:
            if int(answer) == num1 + num2:
                return True
        except ValueError:
            return False
        return False

    # Multiplication
    def question2():
        num1 = random.randint(-25, 25)
        num2 = random.randint(-25, 25)

        answer = input(f"\n{num1} x {num2} = ").strip()

        if answer == "":
            return False

        try:
            if int(answer) == num1 * num2:
                return True
        except ValueError:
            return False
        return False

    # Quadratic Roots 
    def question3():
        a = random.randint(-3, 3)
        b = random.randint(-21, 21)
        c = random.randint(-10, 10)

        quad = Polynomial.set_polynomial(c, b, a, 0, 0, 0)

        D = b ** 2 - 4. * a * c

        print(f"\nSolve for x: {Polynomial.get_polynomial(quad)} = 0")
        print("Please write your answer(s) to 3 decimal places, pressing 'Enter' after each entry.")
        print("If no real solutions exist, press the enter key once.\n")

        if D < 0 and a != 0:
            if input() == "":
                return True

        elif a == 0:
            try:
                if round(float(input()), 3) == round((-c / b), 3):
                    return True
            except ValueError:
                return False

        else:
            root1 = round((-b + math.sqrt(D)) / (2 * a), 3)
            root2 = round((-b - math.sqrt(D)) / (2 * a), 3)

            try:
                if root1 == root2:
                    if round(float(input().strip()), 3) == root1:
                        return True

                else:
                    ans1 = round(float(input().strip()), 3)
                    ans2 = round(float(input().strip()), 3)
                    if (root1 == ans1 and root2 == ans2) or (root2 == ans1 and root1 == ans2):
                        return True
            except ValueError:
                return False

        return False

    def question4():
        """
        Derivative at x of a polynomial.
        """

        a = random.randint(-5, 5)
        b = random.randint(-5, 5)
        c = random.randint(-5, 5)
        d = random.randint(-5, 5)
        e = random.randint(-5, 5)
        f = random.randint(-5, 5)

        Polynomial.set_polynomial(f, e, d, c, b, a)

        seed_for_x = random.randint(-20, 20)

        
        

        
def handle_question(question):
    question_map = {
        1: lambda: Questions.question_text(Questions.question1, 0),
        2: lambda: Questions.question_text(Questions.question2, 1),
        3: lambda: Questions.question_text(Questions.question3, 2),
        4: lambda: Questions.question_text(Questions.question4, 3),
        5: lambda: Questions.question_text(Questions.question5, 4),
        6: lambda: Questions.question_text(Questions.question6, 5),
        7: lambda: Questions.question_text(Questions.question7, 6),
        8: lambda: Questions.question_text(Questions.question8, 7)
    }
    question_map[question]()


print("\nWelcome to the Math Quiz!")
while True:
    selection = input("\nPlease choose a question (1-8). Press 's' to see your current score. Press 'q' to quit: ").lower().strip()

    if selection.startswith('s'):
        print(f"\nCurrent score: {score}/8")
        continue

    if selection == 'q':
        break

    done_index = 3

    if selection.isdigit() and int(selection) in range(1, done_index + 1):
        handle_question(int(selection))
        continue

    if selection.isdigit() and int(selection) in range(done_index + 1, 9):
        print(f"\nQuestion {selection} is currently under construction.")

    else:
        print("\nInvalid selection.")

    if score == 8:
        print("Congratulations! You have answered all of the questions correctly.")
        break
