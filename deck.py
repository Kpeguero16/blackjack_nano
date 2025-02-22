import random
import time


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

        # Assign card values
        if rank == "Ace":
            self.value = 11  # Default to 11, adjusted later if needed
        elif rank in ["Jack", "Queen", "King"]:
            self.value = 10
        else:
            self.value = int(rank)  # Numeric cards 2-10

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        self.cards = self._create_deck()

    def _create_deck(self):
        return [Card(suit, rank) for suit in self.suits for rank in self.ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if not self.cards:
            return None
        return self.cards.pop()

    def __str__(self):
        return ", ".join(str(card) for card in self.cards)


def calculate_hand_value(hand):
    total = sum(card.value for card in hand)
    num_aces = sum(1 for card in hand if card.rank == "Ace")

    # Adjust for aces if the total is over 21
    while total > 21 and num_aces > 0:
        total -= 10  # Treat an Ace as 1 instead of 11
        num_aces -= 1

    return total

def clear_screen():
    """Clears the terminal screen."""
    print("\033[H\033[J", end="")

def display_hands(player_hand, dealer_hand, reveal_dealer=False):
    """
    Displays the player's and dealer's hands, along with their totals.
    If `reveal_dealer` is False, the dealer's first card is hidden.
    """
    clear_screen()

    # Calculate totals
    player_total = calculate_hand_value(player_hand)
    dealer_total = calculate_hand_value(dealer_hand) if reveal_dealer else "?"

    # Display player's hand and total
    print("Blackjack_nano")
    print("--------------\n")
    print("Player's hand:", ", ".join(str(card) for card in player_hand), f"| Total: {player_total}")

    # Display dealer's hand and total
    if reveal_dealer:
        print("Dealer's hand:", ", ".join(str(card) for card in dealer_hand), f"| Total: {dealer_total}")
    else:
        print("Dealer's hand: " + ", ".join(
            str(card) if i == 1 else "?" for i, card in enumerate(dealer_hand)
        ), f"| Total: {dealer_total}")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)