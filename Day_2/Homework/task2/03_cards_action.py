VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
SUITS = ('Spades', 'Clubs', 'Diamonds', 'Hearts')
SUITS_UNI = {
        'Spades': '♠',
        'Clubs': '♣',
        'Diamonds': '♦',
        'Hearts': '♥'
}

class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit    # Масть карты
    def to_str(self):
        return self.value + SUITS_UNI.get(self.suit, "Invalid Suit")

    def equal_suit(self, other_card):
        return self.suit is other_card.suit


    def more(self, other_card):
        if VALUES.index(self.value) > VALUES.index(other_card.value):
            return True
        elif VALUES.index(self.value) < VALUES.index(other_card.value):
            return False
        else:
            if SUITS.index(self.suit) < SUITS.index(other_card.suit):
                return False
            else:
                return True

    def less(self, other_card):
        return not self.more


cards = []
# TODO-1: в список cards добавьте ВСЕ карты всех мастей
for suit in SUITS:
    for value in VALUES:
        cards.append(Card(value, suit))
# TODO-2: Выведите карты в формате: cards[кол-во]2♥, 3♥, 4♥ ... A♥, 2♦, 3♦ ... A♦, ....
formatted_cards = ", ".join([card.to_str() for card in cards])
print(f"cards[{len(cards)}]{formatted_cards}")