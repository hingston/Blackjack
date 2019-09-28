# Radius Interview Python Programming Task
### Purpose
The purpose of this task is for you to demonstrate a basic knowledge of the Python programming language and general programming techniques.
### Task
Write an interactive version of the popular card game Blackjack using the Python programming language. The game should enable a dealer and a single player to play a game of Blackjack using a standard 52 card pack (or deck). There is no requirement to create a graphical user interface, using simple command line prompts to enable the player to interact with the game is sufficient. Use of class based objects is preferable although using functions instead (or a combination of both) is acceptable. If you are unfamiliar with the Blackjack game you can find an overview of the rules below, which can also be found by searching online.

Although you are free to implement as many rules of the game as you wish you are not required to implement all of them, just those that enable a user to play a game of Blackjack against a dealer in its most basic form will be sufficient, providing the ability to place a stake or bet on a hand in a game is also not required.

Some of the rules vary globally so if you are familiar with the Blackjack game feel free to implement the version you are comfortable with. Note that we are not looking for the perfect solution but one that demonstrates your programming experience.

Finally, you should provide a few sentences and/or bullet points detailing what you would do to improve your given solution should you be given the opportunity to develop it further.
## Blackjack Rules
In Blackjack, your objective is to get the value of your hand closer to 21 than the dealer's hand. However, if you exceed 21 you lose automatically (go bust).

Really there are two ways of winning:
* Get the value of your hand closer to 21 than the dealer by drawing more cards
* Stick with your hand and see if the dealer goes bust (in most Blackjack variants the dealer cannot stick on less than 17).

Once you have placed your stake you are dealt 2 cards and the dealer is dealt 1 face up card.
### Blackjack
If you are dealt 21 on your initial hand, it is referred to as a natural Blackjack and you are paid 2.5x your stake. Unless the dealer also shows Blackjack (note a natural Blackjack is the highest hand, worth more than 21, made from 3 or more cards).

Assuming you have not been dealt a Blackjack you can then:
### Stand/Stick
Stand is when you refuse anymore cards, do this when you feel you have a high hand say 17 or more. Or when the dealer shows a low card, (as the dealer must 'hit' on 16 and lower hands), hence there is a fair chance of the dealer going 'BUST' if the dealer were to draw a high card.
### Hit/Twist
Accept an additional card to get your hand value closer to 21, you may do this as many times as you wish as long as your hand remains under 21. However if the additional card you receive takes your hand above 21 you go BUST and lose immediately.

---

# Improvements
If I were to continue development I would improve the following:
* Allow the Deck class to shuffle multiple decks into each other to make card counting more difficult
* Implement all the additional Blackjack rules such as doubling, splitting, etc
* Implement betting - the player can continue until they are bust or cash out
* Implement other games to use my Deck class