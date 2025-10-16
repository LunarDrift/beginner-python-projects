# More OOP Practice
import random

print(r":::       :::     :::     :::::::::  ")
print(r":+:       :+:   :+: :+:   :+:    :+: ")
print(r"+:+       +:+  +:+   +:+  +:+    +:+ ")
print(r"+#+  +:+  +#+ +#++:++#++: +#++:++#:  ")
print(r"+#+ +#+#+ +#+ +#+     +#+ +#+    +#+ ")
print(r" #+#+# #+#+#  #+#     #+# #+#    #+# ")
print(r"  ###   ###   ###     ### ###    ### ")
print("")
print("Rules:  Players compare cards; higher card wins both. If same rank, 'War' occurs, with higher card winning both piles.")
print("")

class Card:
    def __init__(self, rank, suit, value):
        self.rank = rank
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    def __gt__(self, other_card):
        return self.value > other_card.value
    
class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        rank_values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}

        ranks = list(rank_values.keys())
        # Creating the list of Card objects, passing the value to the constructor
        self.cards = [
            Card(rank, suit, rank_values[rank])
            for suit in suits
            for rank in ranks
        ]

    def shuffle(self):
# Shuffles the deck of cards in place
        random.shuffle(self.cards)

    def deal_card(self):
# Deals a single card from the top of the deck
        if len(self.cards) == 0:
            return None
        return self.cards.pop()

    def __len__(self):
# Returns the number of cards left in the deck.
        return len(self.cards)
    
# Create and shuffle the deck
my_deck = Deck()
my_deck.shuffle()


class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def __str__(self):
        # Returns a string representing the player  and number of cards they have. Useful for debugging and printing game state.
        return f"Player {self.name} has {len(self.all_cards)} cards"
    
    def play_card(self, index):
        # Removes and returns a card from a specific index in the player's hand
        if 0 <= index < len(self.all_cards):
            return self.all_cards.pop(index)
        else:
            return None
        
    def remove_one(self):
        # Removes and returns a single card from the top of the Computer player's card list
        if len(self.all_cards) == 0:
            return None
        return self.all_cards.pop(0)
    
    def add_cards(self, new_cards):
        # Adds a single card or a list of cards to player's hand
        # Added to bottom of the deck
        if isinstance(new_cards, list):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def has_cards(self):
        # Returns True if player has cards left, False otherwise
        return len(self.all_cards) > 0
    
    def display_hand(self):
        # Returns a formatted string of the player's cards, each with an index.
        card_strings = [f"[{i+1}] {card}" for i, card in enumerate(self.all_cards)]
        return ", ".join(card_strings)
    
class WarGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)

        # Create and Shuffle deck
        self.deck = Deck()
        self.deck.shuffle()

        # Split the deck between the two players
        self.deal_cards()

    def deal_cards(self):
        while len(self.deck.cards) > 0:
            self.player1.add_cards(self.deck.deal_card())
            self.player2.add_cards(self.deck.deal_card())

    def play_round(self):
        # Plays a single round of the game. Returns True if game is still active, False if a winner is determined.
        # If either player is out of cards, game is over
        if not self.player1.has_cards() or not self.player2.has_cards():
            return False

        print(f"\n--- New Round! ---")

        # Display the human player's hand with indices
        print(f"{self.player1.name}, your hand: ")
        for i, card in enumerate(self.player1.all_cards):
            print(f"[{i+1}] {card}")

        # Get human player's card choice
        while True:
            try:
                choice = int(input("Enter the number of the card you want to play: "))
                player1_card = self.player1.play_card(choice - 1)
                if player1_card is not None:
                    break
                else:
                    print("Invalid card number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Computer plays a random card
        player2_card = self.player2.remove_one()

        player1_pile = [player1_card]
        player2_pile = [player2_card]

        print(f"\n{self.player1.name} plays {player1_pile[0]}")
        print(f"{self.player2.name} plays {player2_pile[0]}\n")

        # Compare cards and determine winner
        self.compare_cards(player1_pile, player2_pile)

        # Check if game is over after round ends
        return self.player1.has_cards() and self.player2.has_cards()
    
    def compare_cards(self, p1_pile, p2_pile):
        p1_card = p1_pile[-1]
        p2_card = p2_pile[-1]

        if p1_card.value > p2_card.value:
            print(f"{self.player1.name} wins the round!\n")
            self.player1.add_cards(p1_pile + p2_pile)
        elif p2_card.value > p1_card.value:
            print(f"{self.player2.name} wins the round!")
            self.player2.add_cards(p1_pile + p2_pile)
        else:
            print("--- War! ---")
            self.war(p1_pile, p2_pile)

    def war(self, p1_pile, p2_pile):
        # Handles the War scenario with a user prompt
        print("--- War! ---")
        input("Press Enter to continue the War! ")

        # Check if players have enough cards for a war
        if len(self.player1.all_cards) < 4 or len(self.player2.all_cards) < 4:
            # If a player runs out of cards during a war, they lose
            if len(self.player1.all_cards) < 4:
                print(f"{self.player1.name} doesn't have enough cards for a war and loses!")
            else:
                print(f"{self.player2.name} doesn't have enough cards for a war and loses!")

            self.player1.all_cards = []
            self.player2.all_cards = []
            return
        
        # Add 3 face-down cards to the pile
        for _ in range(3):
            p1_pile.append(self.player1.remove_one())
            p2_pile.append(self.player2.remove_one())

        # Display the face-up card choices for the human player
        print(f"\n{self.player1.name}, choose your face-up card for the War!")
        print(f"{self.player1.name}, your hand: {self.player1.display_hand()}")
        
        # Human player chooses their final face-up card
        while True:
            try:
                choice = int(input("Enter the number of the card you want to play: "))
                player1_card = self.player1.play_card(choice - 1)
                if player1_card is not None:
                    p1_pile.append(player1_card)
                    break
                else:
                    print("Invalid card number. Please try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter a valid number.")

        # Computer plays their final face-up card from the top of their deck
        player2_card = self.player2.remove_one()
        p2_pile.append(player2_card)

        print(f"\nWar card for {self.player1.name}: {p1_pile[-1]}")
        print(f"War card for {self.player2.name}: {p2_pile[-1]}")

        self.compare_cards(p1_pile, p2_pile)

    def play_game(self):
        round_num = 0
        
        while self.player1.has_cards() and self.player2.has_cards():
            round_num += 1
            print(f"\n=======Round {round_num} =======")
            self.play_round()

            # Print card counts for each player
            print(f"Cards remaining: {self.player1.name}: {len(self.player1.all_cards)}, {self.player2.name}: {len(self.player2.all_cards)}")

            # Break condition to avoid infinite loop
            if round_num > 200:
                print("Game took too long! Ending.")
                break
        self.declare_winner()

    def declare_winner(self):
        if self.player1.has_cards():
            print(f"\n{self.player1.name} wins the game!")
        elif self.player2.has_cards():
            print(f"\n{self.player2.name} wins the game!")
        else:
            print("\nThe game ends in a draw!")

def main():
    # Ask the user for their name
    player_name = input("Enter your name, Player: ")

    game = WarGame(player_name, "Computer")
    game.play_game()

if __name__ == "__main__":
    main()