# Initialize score and done bools

score = 0
done = [False] * 8

while True:
    print("Please choose a question (1-8). Press 's' to see your current score. Press 'q' to quit. ")
    selection = input().lower().strip()

    if selection.startswith('s'):
        print(f"\nCurrent score: {score}/8\n")
        continue

    if selection == 'q':
        break

    if selection.isdigit() and int(selection) in range(1, 9):
        print(f"\nQuestion {selection} is currently under construction.")

    else:
        print("\nInvalid selection.")

    if score == 8:
        print("Congratulations! You have answered all of the questions correctly.")
        break

    