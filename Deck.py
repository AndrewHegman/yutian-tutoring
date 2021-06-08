from cards import Card
from random import shuffle


class Deck:
    """
    A class used to represent a deck of cards

    Attributes:
        __suits: list (str) (private) (static)
            list of suits in a deck of cards
        __ranks: list (str) (private) (static)
            list of ranks in a deck of cards
        __deck: list (Card) (private)
            list of Cards representing a deck of playing cards

    Methods:
        shuffle_deck() -> None
            Randomizes the order of the elements in the deck list

        get_card() -> None, Card
            Returns and removes the card at the front of the list. Returns None if there are no cards in the deck
    """
    __suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
    __ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, shuffle_deck=True):
        """
        Parameters
        ----------
            shuffle_deck: boolean, optional
                If True, the order of the cards will be randomized. Otherwise, the order of the cards will be sorted.
                (Default True).
        """
        self.__deck = [Card(suit, rank) for suit in self.__suits for rank in self.__ranks]
        if shuffle_deck:
            shuffle(self.__deck)

    def shuffle_deck(self):
        """
        Randomizes the order of the elements in the deck list.

        Returns
        -------
        None
        """
        shuffle(self.__deck)

    def get_card(self):
        """
        Returns and removes the first card in the deck list. If there are no cards left in the deck, None is returned.

        Returns
        -------
        Card or None
        """
        if len(self.__deck) > 0:
            return self.__deck.pop()
        return None
