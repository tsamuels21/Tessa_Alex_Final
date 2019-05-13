import random

suits = ["S", "C", "H", "D"]
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]




def shuffle(deck):
    new_deck = []
    while len(deck) > 0:
        card = deck.pop(random.randrange(len(deck)))
        new_deck.append(card)
    return new_deck

deck = []
for card in cards:
    for suit in suits:
        deck.append(card + suit)

print(deck)

new_deck = shuffle(deck)
print(new_deck)
print(len(new_deck))

deal = new_deck[0:5]
print(deal)
print()
