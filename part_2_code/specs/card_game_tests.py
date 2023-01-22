import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    # pass

    def setUp(self):
        self.card_game = CardGame("cards")
        self.card = Card("Hearts", 1)
        self.card1 = Card("Spades", 3)
        self.card2 = Card("Diamonds", 4)


    def test_check_for_ace(self):
        self.assertEqual(True, self.card_game.check_for_ace(self.card))

    def test_highest_card(self):
        self.assertEqual(self.card2, self.card_game.highest_card(self.card1, self.card2))

    def test_cards_total(self):
        cards = [self.card, self.card1, self.card2]
        self.assertEqual("You have a total of 8", self.card_game.cards_total(cards))

