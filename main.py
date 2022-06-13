import random

while True:
    user_action = input("Enter your choice (R, P, S): ")
    possible_actions = ["R", "P", "S"]
    computer_action = random.choice(possible_actions)
    print (f"\nPlayer({user_action}), CPU({computer_action}).\n")

    if user_action not in possible_actions:
        print ("Wrong Choice")

    elif user_action == computer_action:
        print(f"Both Players Selected ({computer_action}). It's a tie!")

    elif user_action == "R":
        if computer_action == "S":
            print("Rock Smashes Scissors! You Win!")
        else:
            print("Paper Covers Rock! You Lose.")

    elif user_action == "P":
        if computer_action == "R":
            print("Paper Covers Rock! You Win!")
        else:
            print("Scissors Cuts Paper! You Lose.")

    elif user_action == "S":
        if computer_action == "P":
            print("Scissors Cuts Paper! You Win!")
        else:
            print("Rock Smashes Scissors! You Lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() !="y":
        break
    