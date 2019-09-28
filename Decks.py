from collections import namedtuple
from itertools import product
from random import shuffle

Card = namedtuple("Card", "suit value")


class Deck:
    suits = []
    values = []

    def __init__(self) -> None:
        self.cards = []
        self.new()

    def __str__(self) -> str:
        return ", ".join(["-".join(card) for card in self.cards])

    def new(self) -> None:
        for card in product(self.suits, self.values):
            self.cards.append(Card(*card))

    def shuffle(self) -> None:
        shuffle(self.cards)

    def draw(self) -> Card:
        return self.cards.pop()

    @property
    def empty(self) -> bool:
        return len(self.cards) == 0


class FrenchDeck(Deck):
    suits = ["C", "D", "H", "S"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
