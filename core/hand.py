from functools import reduce
from core.card import Card

class Hand:
    def __init__(self, owner: str):
        self.owner = owner
        self.cards = []

    def add_card(self, card: Card):    
        self.cards.append(card)
    
    def clear_card(self):
        self.cards = []
    
    def total(self, hidden = False) -> int:
        def sum_condition (b):
            index = self.cards.index(b) + 1
            return 0 if hidden and index % 2 == 0 else b.value
        return reduce(lambda a,b: a + sum_condition(b), self.cards, 0)

    def is_blackjack(self):
        return self.total() == 21

    def card_detail(self, crd):
        return f"{crd.rank.title()} of {crd.suit}\n"

    def get_details(self, hidden = False):        
        return reduce(lambda a, b: a + self._reduce_handler_get_details(a, b, hidden), self.cards, f"""""")
        
    def _reduce_handler_get_details(self, a, b, hidden = False):
        index = self.cards.index(b) + 1
        card_hidden = "Hidden card\n"

        return card_hidden if index % 2 == 0 and hidden == True else self.card_detail(b)
