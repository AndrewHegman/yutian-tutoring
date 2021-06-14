from Deck import Deck
from account import Account
from Hand import Hand
from cards import Card
from Player import Human

# Using the new Deck class, create a deck
deck = Deck()
# Create a new User
human = Human('JerryTNT')
# Ask the user how much they want to bet
# If the user tries to withdraw more money than they have, end the game immediately--we will improve this later

bet = human.place_bet()
# Draw two cards from the Deck and add to the user's hand (check the methods on the Deck class for help :) )
playercard = deck[0] and deck[1]
deck -= playercard
hand = []
hand += playercard
# Show the user their current cards and ask them if they want to hit_or_stand
print(hand)

# If the user decides to HIT, add another card to their hand
# If the user decides to STAND, end the loop (we will change this next week)

# If the user's card value ever goes above 21, end the loop immediately and print a message saying the user "busted"
