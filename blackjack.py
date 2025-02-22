#!/usr/bin/env python3

import argparse
from deck import *

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="A simple Blackjack game")
    parser.add_argument("--name", type=str, help="Your name")
    args = parser.parse_args()

    # Welcome message
    print(f"Hello, {args.name or 'User'}!\nWelcome to Blackjack_nano!\n")
    time.sleep(2)

    # Initialize deck and hands
    deck = Deck()
    deck.shuffle()

    player_hand = []
    dealer_hand = []

    # Step 1: Initial empty hands
    clear_screen()
    display_hands(player_hand, dealer_hand)

    # Step 2: Deal player's first card
    player_hand.append(deck.deal())
    display_hands(player_hand, dealer_hand)

    # Step 3: Deal dealer's first card (hidden)
    dealer_hand.append(deck.deal())
    display_hands(player_hand, dealer_hand)

    # Step 4: Deal player's second card
    player_hand.append(deck.deal())
    display_hands(player_hand, dealer_hand)

    # Step 5: Deal dealer's second card (visible)
    dealer_hand.append(deck.deal())
    display_hands(player_hand, dealer_hand)

    # Step 6: Reveal dealer's hidden card
    time.sleep(1)
    display_hands(player_hand, dealer_hand, reveal_dealer=True)

if __name__ == "__main__":
    main()