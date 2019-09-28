from collections import namedtuple
from itertools import product
from random import shuffle

Card = namedtuple("Card", "suit value")


class Deck:
    """Base class for a deck of cards

    Attributes:
        suits: A list of suits
        values: A list of values
    """
    suits = []
    values = []

    def __init__(self) -> None:
        """Inits a deck with cards"""
        self.cards = []
        self.new()

    def __str__(self) -> str:
        """Converts a list of cards to a short human readable string.

        For example: [(Diamonds, 6), (Diamonds, 5), (Spades, K)] -> D-6, D-5, S-K
        """
        return ", ".join(["-".join(card) for card in self.cards])

    def new(self) -> None:
        """Adds a full new set of cards to the deck based on the suit and values attributes."""
        for card in product(self.suits, self.values):
            self.cards.append(Card(*card))

    def shuffle(self) -> None:
        """Randomly shuffles the deck"""
        shuffle(self.cards)

    def draw(self) -> Card:
        """Draws a card from the end of the deck

        Simulates taking a card from the top of a face down deck.

        Returns:
            A card

        Raises:
            IndexError if the deck is empty.
        """
        try:
            return self.cards.pop()
        except IndexError:
            raise IndexError("The deck is empty!")

    @property
    def empty(self) -> bool:
        """Property of deck stating if deck is empty or not"""
        return len(self.cards) == 0


class FrenchDeck(Deck):
    """A French deck of cards that inherits from class Deck

    A classic French deck of playing cards. https://en.wikipedia.org/wiki/French_playing_cards

    Attributes:
        suits: A list of suits. Clubs, Diamonds, Hearts and Spades
        values: A list of values. Ace, 2-10, Jack, Queen and King
    """
    suits = ["C", "D", "H", "S"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
