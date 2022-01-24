def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("---------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D: ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guess)

def check_answer(answer, guess):

    if answer == guess:
        print("→ CORRECT!")
        return 1
    else:
        print("→ WRONG!")
        return 0


def display_score(correct_guess, guesses):
    print("--------------------")
    print("RESULTS")
    print("--------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guess/len(questions))*100)
    print(f"Your score is: {score}%.")

def play_again():

    response = input("Do you wanna play again?: (y / n): ")
    response = response.upper()

    if response == "Y":
        return True
    else:
        return False

# --------------------------

questions = {
    "Who create Python? ": "A",
    "What year was Python created?" : "B",
    "Python is tributed to which comedy group? " : "C",
    "Is the Earth round? " : "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
           ["A. 1898", "B. 1991", "C. 1994", "D. 2000"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. True", "B. False", "C. Sometimes", "D. What's Earth?"]]

new_game()

while play_again():
    new_game()

print("See you next time!")
