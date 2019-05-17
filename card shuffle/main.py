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
        self.hand_one = ["" for x in range(1)]
        self.hand_two = ["" for x in range(1)]
        self.history = []
        self.deck = Deck()
        self.cards_one = [self.card0]
        self.cards_two = [self.card2]

    def hit_me_one(self):
        self.card2.image_file = "pic/gray_back.png"
        next_card = 1 - self.hand_one.count("")
        self.hand_one[next_card] = self.deck.card_names.pop(random.randrange(len(self.deck.card_names)))
        for i in range(next_card + 1):
            filename = "pic/"+self.hand_one[i]+".png"
            self.cards_one[i].image_file = filename
            self.history.append(self.hand_one)
            self.hand_one = ["" for x in range(1)]
        print(self.history)

    def high_low(self):
        next_card = 1 - self.hand_two.count("")
        self.hand_two[next_card] = self.deck.card_names.pop(random.randrange(len(self.deck.card_names)))
        for i in range(next_card + 1):
            filename = "pic/"+self.hand_two[i]+".png"
            self.cards_two[i].image_file = filename
            self.history.append(self.hand_two)
            self.hand_one = ["" for x in range(1)]
        print(self.history)


if __name__ == "__main__":
    app = CardsApp()
    app.run()