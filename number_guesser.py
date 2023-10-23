import random


def play_game():
    low = 1
    high = 50
    chances = 5

    print("Welcome to the Number Guesser Game!")
    print("Guess a number between {} and {}.".format(low, high))

    correct_answer = random.randrange(low, high + 1)

    for attempt in range(chances):
        print("\nYou have {} chances left.".format(chances - attempt))
        guess = int(input("Enter your guess: "))

        if guess < correct_answer:
            print("Correct answer is greater!")
        elif guess > correct_answer:
            print("Correct answer is smaller!")
        else:
            print("Congratulations! You Win!")
            break

    if guess != correct_answer:
        print("\nYou lose! The correct answer was:", correct_answer)

    print("\nGame Over!\n")


def play_again():
    choice = input("Do you want to play again? (yes/no): ")
    if choice.lower() == "yes":
        play_game()
        play_again()
    else:
        print("\nThank you for playing!")


play_game()
play_again()
