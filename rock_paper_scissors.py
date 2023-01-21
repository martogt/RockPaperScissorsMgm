import random
import colorama
colorama.init(autoreset=True)

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
computer_move = ""

player_move = input("Choose [r]ock, [p]aper, [s]cissors:")

if player_move.lower() == "r":
    player_move = rock
elif player_move.lower() == "p":
    player_move = paper
elif player_move.lower() == "s":
    player_move = scissors
else:
    raise SystemExit("invalid Input. Try again...")

computer_random_number = random.randint(1, 3)

if computer_random_number == 1:
    computer_move = rock
elif computer_random_number == 2:
    computer_move = paper
elif computer_random_number == 3:
    computer_move = scissors
else:
    raise SystemExit("invalid Input. Try again...")

print(f"The computer chose {computer_move}")

if (player_move == rock and computer_move == scissors) or (player_move == paper and computer_move == rock) or (
        player_move == scissors and computer_move == paper):
    print("You win!")
elif player_move == computer_move:
    print(f"Draw!")
else:
    print("You lose!")

while True:
    play_again = input(f"Do you want to restart? {colorama.Fore.RED}Yes or No\n")

    if play_again.lower() == "y":
        exec(open("./rock_paper_scissors.py").read())
    elif play_again.lower() == "n":
        exit()
    else:
        print("Incorrect answer!")
        continue
