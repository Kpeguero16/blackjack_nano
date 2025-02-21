#!/usr/bin/env python3

import argparse
from deck import Deck  # Importing our Deck class from deck.py

def main():
    parser = argparse.ArgumentParser(description="A simple Blackjack game")
    parser.add_argument("--name", type=str, help="Your name")
    args = parser.parse_args()

    print(f"Hello, {args.name or 'User'}!\nWelcome to Blackjack_nano!")

    # Create a deck, display the original deck, shuffle it, deal a card, and show the remaining deck.
    deck = Deck()
    print("\nOriginal deck:")
    print(deck)

    deck.shuffle()
    print("\nShuffled deck:")
    print(deck)

    print("\nDealing a card:")
    card = deck.deal()
    print(card)

    print("\nRemaining deck:")
    print(deck)

if __name__ == "__main__":
    main()