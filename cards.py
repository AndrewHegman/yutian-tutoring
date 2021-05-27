class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def get_value(self):
        if self.rank == 'A':
            return 11
        elif self.rank == 'J' or self.rank == 'Q' or self.rank == 'K':
            return 10
        else:
            return int(self.rank)

    # Overriding
    # Less than
    def __lt__(self, card):
        return self.rank < card.rank

    # Less than or equal to
    def __lte__(self, card):
        return self.rank <= card.rank

    # Greater than
    def __gt__(self, card):
        return self.rank > card.rank

    # Greater than or equal to
    def __gte__(self, card):
        return self.rank >= card.rank

    # Equal to
    def __eq__(self, card):
        return self.rank == card.rank

    # Not equal to
    def __neq__(self, card):
        return self.rank != card.rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'

    def __repr__(self):
        return f'{self.rank} of {self.suit}'

    def __add__(self, card):
        return self.rank + card.rank
