from typing import List

from Decks import FrenchDeck, Card


class Blackjack:
    """Used to play a simple game of Blackjack

    Plays a game of Blackjack using the console. A single player plays against the dealer. The player has the option of
    hitting or standing. The dealer must hit when on or below 17. The player wins by having a hand value greater than
    that of the dealer.

    Attributes:
        dealer_hand: A list of cards in the players hand.
        player_hand: A list of cards in the dealers hand.
    """
    dealer_hand = []
    player_hand = []

    def __init__(self, deck: FrenchDeck) -> None:
        """Inits Blackjack class with a French deck of cards"""
        self.deck = deck

    @staticmethod
    def max_hand_value(hand: List[Card]) -> int:
        """Calculates maximum hand value

        Calculates the maximum value of a Blackjack hand. This is done by first looping through a hand adding the value
        the card if a number, 10 for kings/queens/jacks and 11 for aces while counting the number of aces. Then looping
        a final time for the number of aces in the hand and subtracting 10 while the score is higher than 21. This
        ensures the maximum hand value is found when there are more than 1 ace in the hand without having to sort the
        before the initial loop.

        Args:
            hand: A list of cards

        Returns:
            An integer of the maximum hand value
        """
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
        """Converts a list of cards to a short human readable string.

        For example: [(Diamonds, 6), (Diamonds, 5), (Spades, K)] -> D-6, D-5, S-K

        Args:
            hand: A list of cards

        Returns:
            A string with a short human readable hand.
        """
        return ", ".join(["-".join(card) for card in hand])

    def print_current_hands(self) -> None:
        """Displays the dealer and player's current hand value and cards"""
        print("Dealer: %02d - Hand: %s." % (self.max_hand_value(self.dealer_hand), self.hand_to_str(self.dealer_hand)))
        print("Player: %02d - Hand: %s." % (self.max_hand_value(self.player_hand), self.hand_to_str(self.player_hand)))

    def play(self) -> None:
        """"""
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
