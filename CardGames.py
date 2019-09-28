from typing import List

from Decks import Deck, Card


class Blackjack:
    dealer_hand = []
    player_hand = []

    def __init__(self, deck: Deck) -> None:
        self.deck = deck

    @staticmethod
    def max_hand_value(hand: List[Card]) -> int:
        score = 0
        aces = 0
        for card in hand:
            if card.value in ["J", "Q", "K"]:
                score += 10
            elif card.value == "A":
                aces += 1
                score += 11
            else:
                score += int(card.value)
        for _ in range(aces):
            if score <= 21:
                break
            else:
                score -= 10
        return score

    @staticmethod
    def hand_to_str(hand: List[Card]) -> str:
        return ", ".join(["-".join(card) for card in hand])

    def print_current_hands(self) -> None:
        print("Dealer: %02d - Hand: %s." % (self.max_hand_value(self.dealer_hand), self.hand_to_str(self.dealer_hand)))
        print("Player: %02d - Hand: %s." % (self.max_hand_value(self.player_hand), self.hand_to_str(self.player_hand)))

    def play(self) -> None:
        self.deck.shuffle()
        play_again = True
        play_forever = False
        while play_again:
            print("\nWelcome to Blackjack!\n")
            self.dealer_hand = []
            self.player_hand = []
            if self.deck.empty:
                self.deck.new()
                self.deck.shuffle()
            self.dealer_hand.append(self.deck.draw())
            self.player_hand.append(self.deck.draw())
            dealer_hidden_card = self.deck.draw()
            self.player_hand.append(self.deck.draw())
            self.print_current_hands()
            player_score = self.max_hand_value(self.player_hand)
            player_bust = False
            while not player_bust:
                reply = str(input("Would you like to (h)it or (s)tand?: ")).lower().strip()[:1]
                if reply == "h":
                    self.player_hand.append(self.deck.draw())
                    self.print_current_hands()
                    player_score = self.max_hand_value(self.player_hand)
                    if player_score > 21:
                        print("BUST - Dealer wins!")
                        player_bust = True
                if reply == "s":
                    break
            if not player_bust:
                self.dealer_hand.append(dealer_hidden_card)
                while self.max_hand_value(self.dealer_hand) < max(17, player_score):
                    self.dealer_hand.append(self.deck.draw())
                self.print_current_hands()
                if player_score <= self.max_hand_value(self.dealer_hand) <= 21:
                    print("Dealer wins!")
                else:
                    print("Player wins!")
            if not play_forever:
                reply = ""
                while reply not in ["y", "n", "f"]:
                    reply = str(input("Would you like to play again? (y)es, (n)o or play (f)orever: ")).lower()[:1]
                    if reply == "y":
                        pass
                    if reply == "n":
                        play_again = False
                    if reply == "f":
                        play_forever = True
