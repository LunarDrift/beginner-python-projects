import random


print(r"  _____            _____ ______   _______ ____    ___   ___  _ ")
print(r" |  __ \     /\   / ____|  ____| |__   __/ __ \  |__ \ / _ \| |")
print(r" | |__) |   /  \ | |    | |__       | | | |  | |    ) | | | | |")
print(r" |  _  /   / /\ \| |    |  __|      | | | |  | |   / /| | | | |")
print(r" | | \ \  / ____ \ |____| |____     | | | |__| |  / /_| |_| |_|")
print(r" |_|  \_\/_/    \_\_____|______|    |_|  \____/  |____|\___/(_)")
print("")
print("")
                                                               
                                                               


def roll_die():
    return random.randint(1, 6)

play_again = "yes"
while play_again.lower() in ["yes", "y"]:


    player1_score = 0
    cpu_score = 0

    print("Rules: Players take turns rolling a die. Each roll adds to their total.\n First to reach or pass 20 points wins\n")

    while player1_score < 20 and cpu_score < 20:
        input("Player: Press Enter to roll the die...\n")
        roll = roll_die()
        player1_score += roll
        print(f"Player rolled a {roll}. Player Total: {player1_score}")

        if player1_score >= 20:
            break
        
        cpu_roll = roll_die()
        cpu_score += cpu_roll
        print(f"The CPU rolled a {cpu_roll}. CPU Total: {cpu_score}\n")

    if player1_score >= 20:
        print("Player 1 wins!")
    else:
        print("The CPU wins!")

    play_again = input("\nDo you want to play again? yes/no: ")
print("Thanks for playing!")