# Rock Paper Scissors

# get user choice
# get computer choice
# compute each round winner
# compute game winner


import random


choices = ["rock", "paper", "scissors"]


# get user choice
def user_choice():

    while True:
        user = input("Please enter a choice: ")
        try:
            if user not in choices:
                continue
            else:
                return user
        except:
            pass


# get computer choice
def computer_choice():
    computer = random.choice(choices)
    print("Computer Choice: " + computer)
    return computer


# get rounds
def menu():

    print("Let's play " + " ".join(choices) + "!")

    # limit odd rounds and number of rounds
    # handle potential exception
    while True:
        try:
            rounds = int(input("How many odd rounds? "))
            if rounds % 2 != 0 and rounds <= 21:
                return rounds
            else:
                continue
        except ValueError:
            print("Exception, please enter an odd number of rounds")


# get score
# get game winner
def play_game():
    odd_rounds = menu()
    user_score = 0
    comp_score = 0
    round_count = 1

    while user_score < odd_rounds/2 and comp_score < odd_rounds/2:

        print("ROUND: " + str(round_count))

        round_winner = round(user_choice(), computer_choice())

        if round_winner == "user":
            user_score += 1
            round_count += 1
            print("You win round")

        elif round_winner == "comp":
            comp_score += 1
            round_count += 1
            print("Computer wins round")
        elif round_winner == "tie":
            print("TIE")

        print("User Score: " + str(user_score))
        print("Computer Score: " + str(comp_score))

    if user_score > comp_score:
        print("YOU WIN!!")
    else:
        print("COMPUTER WINS!")


# get round winner
def round(user, comp):

    if user == comp:
        return "tie"

    elif user == "paper":
        if comp == "rock":
            return "user"
        elif comp == "scissors":
            return "comp"

    elif user == "rock":
        if comp == "scissors":
            return "user"
        elif comp == "paper":
            return "comp"

    elif user == "scissors":
        if comp == "paper":
            return "user"
        elif comp == "rock":
            return "comp"


if __name__ == "__main__":
    play_game()