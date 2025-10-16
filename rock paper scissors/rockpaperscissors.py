# OOP PRACTICE

import random

class RockPaperScissors:
    def __init__(self):
        self.moves = {1: "Rock", 2: "Paper", 3: "Scissors"}
        print("Welcome to Rock, Paper, Scissors!")

    def get_player_move(self):
        while True:
            try:
                player_move = int(input("Select your move. 1 for Rock, 2 for Paper, 3 for Scissors: "))

                if player_move in self.moves:
                    return player_move
                
                else:
                    print("Invalid input. Please enter 1, 2, or 3.")

            except ValueError:
                print("Invalid input. Please enter a number.\n")
            
    def get_cpu_move(self):
        return random.randint(1,3)
    
    def determine_winner(self, player_move, cpu_move):
        print(f"Computer chose {self.moves[cpu_move]}. You chose {self.moves[player_move]}.")

        if player_move == cpu_move:
            print("It's a tie!")
        
        elif (player_move == 1 and cpu_move == 3) or \
        (player_move == 2 and cpu_move == 1) or \
        (player_move == 3 and cpu_move == 2):
            print("You win!")
        else:
            print("You lose!")

    def play(self):
        while True:
            player_move = self.get_player_move()
            cpu_move = self.get_cpu_move()
            self.determine_winner(player_move, cpu_move)

            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() not in ["yes", "y"]:
                print("Thanks for playing!")
                break

game = RockPaperScissors()
game.play()