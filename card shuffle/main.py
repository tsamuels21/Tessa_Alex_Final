import random

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.size = [400, 600]
Window.clearcolor = [0, 0, 0, 1]


class CardsApp(App):
    def build(self):
        return CardTable()


class Deck():
    def __init__(self):
        self.suits = ["S", "D", "H", "C"]
        self.cards = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
        self.card_names = []
        for suit in self.suits:
            for card in self.cards:
                self.card_names.append(card+suit)

        print(len(self.card_names))


class CardTable(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hand = ["" for x in range(5)]
        self.deck = Deck()
        self.cards = [self.card0, self.card1]

    def deal_hand_one(self, number_cards):
        for card in self.cards:
            card.image_file = "pic/gray_black.png"

        self.hand = ["" for x in range(5)]

        for i in range(number_cards):
            self.hand[i] = self.deck.card_names.pop(random.randrange(len(self.deck.card_names)))

        for i in range(number_cards):
            filename = "pic/"+self.hand[i]+".png"
            self.cards[i].image_file = filename
        print(self.hand)

    def hit_me_one(self):
        next_card = 5 - self.hand.count("")
        self.hand[next_card] = self.deck.card_names.pop(random.randrange(len(self.deck.card_names)))
        for i in range(next_card + 1):
            filename = "pic/"+self.hand[i]+".png"
            self.cards[i].image_file = filename
        print(self.hand)

    def deal_hand_two(self, number_cards):
        for card in self.cards:
            card.image_file = "pic/gray_black.png"

        self.hand = ["" for x in range(5)]

        for i in range(number_cards):
            self.hand[i] = self.deck.card_names.pop(random.randrange(len(self.deck.card_names)))

        for i in range(number_cards):
            filename = "pic/"+self.hand[i]+".png"
            self.cards[i].image_file = filename
        print(self.hand)

    def hit_me_two(self):
        next_card = 5 - self.hand.count("")
        self.hand[next_card] = self.deck.card_names.pop(random.randrange(len(self.deck.card_names)))
        for i in range(next_card + 1):
            filename = "pic/"+self.hand[i]+".png"
            self.cards[i].image_file = filename
        print(self.hand)


if __name__ == "__main__":
    app = CardsApp()
    app.run()