class Hand:
    def __init__(self):
        self.__cards = []
        self.__value = 0
        self.__aces = 0
        # HINT: You may need to add some new variables here to keep track of ACES...hmmmmmm

    def add_card(self, card):
        if card.rank == 'A':
            self.__aces += 1
        self.__cards.append(card)
        self.__value += card.get_value()
        if self.__value > 21 and self.__aces >= 1:
            self.__value -= 10
            self.__aces -= 1
        # You will need to figure out how to figure out if there are any ACES that can be converted to a 1 instead of an 11 (this will be challenging!)

    def get_cards_str(self, limit=None):
        s = '['
        for i, card in enumerate(self.__cards):
            if i == limit:
                break
            s += str(card)
            if i < len(self.__cards) - 1:
                s += ', '

        s += ']'
        return s

    def get_value(self):
        return self.__value

