from account import Account
from Hand import Hand
from cards import Card
account = Account(0, 'Jerry')
account.withdraw(10)
print(account.get_balance())

# Using the new Deck class, create a deck

# Create a new User

# Ask the user how much they want to bet

# Draw two cards from the Deck and add to the user's hand (check the methods on the Deck class for help :) )

# Show the user their current cards and ask them if they want to hit_or_stand

# If the user decides to HIT, add another card to their hand
# If the user decides to STAND, end the loop (we will change this next week)

# If the user's card value ever goes above 21, end the loop immediately and print a message saying the user "busted"
