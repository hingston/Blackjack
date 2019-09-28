from CardGames import Blackjack
from Decks import FrenchDeck


def main() -> None:
    deck = FrenchDeck()
    game = Blackjack(deck)
    game.play()


if __name__ == "__main__":
    main()
