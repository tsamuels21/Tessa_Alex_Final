import random

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.popup import Popup

Window.size = [400, 600]
Window.clearcolor = [0, 0, 0, 1]


class CardsApp(App):
    def build(self):
        return CardTable()


class CustPopupLose(Popup):
    table = None


class Deck():
    def __init__(self):
        self.suits = ["S", "D", "H", "C"]
        self.cards = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
        self.card_names = []
        for suit in self.suits:
            for card in self.cards:
                self.card_names.append(card+suit)


class CardTable(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hand_one = ["" for x in range(1)]
        self.hand_two = ["" for x in range(1)]
        self.deck = Deck()
        self.cards_one = [self.card0]
        self.cards_two = [self.card2]
        self.number_one = []
        self.number_two = []
        self.number = []
        self.x = 0
        self.num_two = []
        self.y = 0
        self.cards = ["A", "K", "Q", "J", "1", "9", "8", "7", "6", "5", "4", "3", "2"]
        self.score = 0
        self.pop = CustPopupLose()
        self.pop.table = self

    def popup(self):
        self.pop.open()

    def popclose(self):
        self.pop.dismiss()

    def hit_me_one(self):
        if self.x == 0:
            self.x = 1
            self.number.clear()
            self.card2.image_file = "pic/red_back.png"
            next_card = 1 - self.hand_one.count("")
            self.hand_one[next_card] = self.deck.card_names.pop(random.randrange(len(self.deck.card_names)))
            for i in range(next_card + 1):
                filename = "pic/" + self.hand_one[i] + ".png"
                self.cards_one[i].image_file = filename
                self.number_one = [x[0] for x in self.hand_one]
                self.number.append(self.number_one)
                self.hand_one = ["" for x in range(1)]

    def value(self):
        if self.x == 1:
            next_card = 1 - self.hand_two.count("")
            self.hand_two[next_card] = self.deck.card_names.pop(random.randrange(len(self.deck.card_names)))
            for i in range(next_card + 1):
                filename = "pic/" + self.hand_two[i] + ".png"
                self.cards_two[i].image_file = filename
                self.number_two = [x[0] for x in self.hand_two]
                self.number.append(self.number_two)
                self.hand_two = ["" for x in range(1)]
        self.x = 0

    def reset(self):
        self.hand_one = ["" for x in range(1)]
        self.hand_two = ["" for x in range(1)]
        self.deck = Deck()
        self.cards_one = [self.card0]
        self.cards_two = [self.card2]
        self.number_one = []
        self.number_two = []
        self.number = []
        self.x = 0
        self.num_two = []
        self.y = 0
        self.cards = ["A", "K", "Q", "J", "1", "9", "8", "7", "6", "5", "4", "3", "2"]
        self.score = 0
        self.card2.image_file = "pic/red_back.png"
        self.card0.image_file = "pic/red_back.png"
        self.popclose()

    def high_check(self):
        self.value()
        if self.cards.index(self.number[0][0]) > self.cards.index(self.number[1][0]):
            self.score += 1
        else:
            self.popup()

    def low_check(self):
        self.value()
        if self.cards.index(self.number[0][0]) < self.cards.index(self.number[1][0]):
            self.score += 1
        else:
            self.popup()


if __name__ == "__main__":
    app = CardsApp()
    app.run()
