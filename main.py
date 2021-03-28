import random


def main():
    Answer = input("Make a move! (Rock/Paper/Scissors): ").lower()
    Options = ["rock", "paper", "scissors"]
    CpuTurn = random.choice(Options)
    if Answer == "rock":
        print("You chose rock")
        print("Your opponent chose " + CpuTurn)
        if CpuTurn == "rock":
            print("You both chose rock. It's a tie!")
            again = input("Play again? (yes/no): ").lower()
            if again == "yes":
                main()
            else:
                quit()
        elif CpuTurn == "scissors":
            print("Rock beats scissors. You win!")
            again = input("Play again? (yes/no): ").lower()
            if again == "yes":
                main()
            else:
                quit()
        elif CpuTurn == "paper":
            print("Paper beats rock. You lose!")
            again = input("Play again? (yes/no): ").lower()
            if again == "yes":
                main()
            else:
                quit()
    if Answer == "scissors":
        print("You chose scissors")
        print("Your opponent chose " + CpuTurn)
        if CpuTurn == "rock":
            print("Rock beats scissors. You lose!")
            again = input("Play again? (yes/no): ").lower()
            if again == "yes":
                main()
            else:
                quit()
        elif CpuTurn == "scissors":
            print("You both chose scissors. It's a tie!")
            again = input("Play again? (yes/no): ").lower()
            if again == "yes":
                main()
            else:
                quit()
        elif CpuTurn == "paper":
            print("Scissors beats paper. You win!")
            again = input("Play again? (yes/no): ").lower()
            if again == "yes":
                main()
            else:
                quit()
    if Answer == "paper":
        print("You chose paper")
        print("Your opponent chose " + CpuTurn)
        if CpuTurn == "rock":
            print("Paper beats rock. You win!")
            again = input("Play again? (yes/no): ").lower()
            if again == "yes":
                main()
            else:
                quit()
        elif CpuTurn == "scissors":
            print("Scissors beats paper. You lose!")
            again = input("Play again? (yes/no): ").lower()
            if again == "yes":
                main()
            else:
                quit()
        elif CpuTurn == "paper":
            print("You both chose paper. It's a tie!")
            again = input("Play again? (yes/no): ").lower()
            if again == "yes":
                main()
            else:
                quit()
    else:
        print("Not a valid input. Please type either rock, paper, or scissors")
        main()


    return main

main()



