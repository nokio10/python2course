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


hearts_cards = []
for value in VALUES:
    hearts_cards.append(Card(value, 'Hearts'))
# TODO-1: добавьте в список hearts_cards все червовые карты(от 2-ки до туза)

diamonds_cards = []
# TODO-2: добавьте в список diamonds_cards все бубновые карты(от туза до 2-ки)
for value in VALUES:
    hearts_cards.append(Card(value, 'Diamonds'))
# TODO-3: выведите все карты из списка hearts_cards в терминал через запятую в одну строку:
# Пример вывода: 2♥, 3♥, 4♥ ... A♥
print([card.to_str() for card in hearts_cards])
