import random

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
        Polynomial.coefficient_list.append(pow5)
        Polynomial.coefficient_list.append(pow4)
        Polynomial.coefficient_list.append(pow3)
        Polynomial.coefficient_list.append(pow2)
        Polynomial.coefficient_list.append(pow1)
        Polynomial.coefficient_list.append(pow0)
        return True

    def get_polynomial(self):
        polynomial_set = []
        zeros_count = 0

        for i in range(len(Polynomial.coefficient_list)):
            print(i)

class Questions:
    @staticmethod
    def question_text(q, done_index):
        global done
        global score
        if done[done_index]:
            print("\nYou have already answered this question correctly.\n")
        else:
            if q():
                score += 1
                done[done_index] = True
                print("\nCorrect!")
                print(f"Current score: {score}/8\n")

            else:
                print("\nIncorrect answer.")
                print(f"Current score: {score}/8\n")

    def question1():
        num1 = random.randint(-100, 100)
        num2 = random.randint(-100, 100)

        if num2 < 0:
            answer = input(f"\n{num1} - {-1 * num2} = ").strip()
        else:
            answer = input(f"\n{num1} + {num2} = ").strip()

        if answer is "":
            return False

        elif int(answer) == num1 + num2:
            return True
        else:
            return False

    # Multiplication
    def question2():
        num1 = random.randint(-25, 25)
        num2 = random.randint(-25, 25)

        answer = input(f"\n{num1} x {num2} = ").strip()

        if answer is "":
            return False

        elif int(answer) == num1 * num2:
            return True
        else:
            return False

    # Quadratic Roots 
    def question3():
        a = random.randint(-3, 3)
        b = random.randint(-21, 21)
        c = random.randint(-10, 10)



        
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
        print(f"\nCurrent score: {score}/8\n")
        continue

    if selection == 'q':
        break

    if selection.isdigit() and int(selection) in range(1, 3):
        handle_question(int(selection))
        continue

    if selection.isdigit() and int(selection) in range(3, 9):
        print(f"\nQuestion {selection} is currently under construction.")

    else:
        print("\nInvalid selection.")

    if score == 8:
        print("Congratulations! You have answered all of the questions correctly.")
        break
