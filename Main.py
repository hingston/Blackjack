from Decks import FrenchDeck
from CardGames import Blackjack


def main() -> None:
    deck = FrenchDeck()
    game = Blackjack(deck)
    game.play()


if __name__ == "__main__":
    main()
