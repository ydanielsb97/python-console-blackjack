from core.card import Card
from core.constants import RANKS, SUITS
import random

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                card = (suit, rank[0], rank[1])
                self.cards.append(Card(card))
    
    def _get_random_card(self):
        random_card = random.choice(self.cards)
        self.cards.remove(random_card)
        return random_card