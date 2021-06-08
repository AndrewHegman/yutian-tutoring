from Hand import Hand
from account import Account
from Utils import safe_number_input


class User:
    def __init__(self, user_name, account_balance=0):
        self.account = Account(account_balance, user_name)
        self.hand = Hand()

    def hit_or_stand(self):
        pass

    def show_cards(self, num):
        pass

    def add_card(self, card):
        pass


class Human(User):
    def __init__(self, user_name, account_balance=100):
        User.__init__(self, user_name, account_balance)

    def hit_or_stand(self):
        print(f'Your current hand is {self.hand.get_value()}')
        return safe_number_input('Do you want to hit(1) or stand(2)?', [1, 2])

    def show_cards(self, num=None):
        print(self.hand.get_cards_str())

    def place_bet(self):
        print(f'you currently have ${self.account.get_balance()}')
        amount = safe_number_input('how much do you want to place?!?!?!?!?!?!    ')
        self.account.withdraw(amount)

    def add_card(self, card):
        self.hand.add_card(card)


class Dealer(User):
    def __init__(self):
        User.__init__(self, user_name='Mr. Fat')

    def hit_or_stand(self):

        if self.hand.get_value() < 17:
            return 1
        else:
            return 2

    def show_cards(self, num):
        print(self.hand.get_cards_str(num))

    def add_card(self, card):
        self.hand.add_card(card)

