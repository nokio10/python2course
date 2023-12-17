import random

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
        self.suit = suit  # Масть карты

    def __str__(self):
        return self.value + SUITS_UNI[self.suit]

    def __repr__(self):
        return str(self)

    def equal_suit(self, other_card) -> bool:
        return self.suit == other_card.suit

    def more(self, other_card) -> bool:
        if self.value == other_card.value:
            return SUITS.index(self.suit) > SUITS.index(other_card.suit)
        return VALUES.index(self.value) > VALUES.index(other_card.value)

    def less(self, other_card) -> bool:
        # Можно и так, но пока лучше все прописывать
        # return not self.more(other_card)
        if self.value == other_card.value:
            return SUITS.index(self.suit) < SUITS.index(other_card.suit)
        return VALUES.index(self.value) < VALUES.index(other_card.value)


# Задание: Теперь создадим колоду из 52-ух карт и реализуем все методы
class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        self.cards = []
        for suit in SUITS:
            for value in VALUES:
                self.cards.append(Card(value, suit))

    def __str__(self):
        return ' '.join(str(card.value) + SUITS_UNI[card.suit] for card in self.cards)

    def __repr__(self):
        return str(self)

    def show(self):
        # Принцип работы данного метода прописан в 00_task_deck.md
        print(self.cards)

    def draw(self, x):
        # Принцип работы данного метода прописан в 00_task_deck.md
        x *= x > 0
        drawn_cards = self.cards[:x]  # Возвращает список из x первых карт
        self.cards = self.cards[x:]  # Убирает эти карты из колоды
        return drawn_cards

    def shuffle(self):
        random.shuffle(self.cards)


# Создаем колоду
deck = Deck()

# Выводим колоду
deck.show()

# Тасуем колоду
deck.shuffle()
deck.show()

# Возьмем 5 карт "в руку"
hand = deck.draw(5)

# Выводим колоду, чтобы убедиться что 5 верхних карт отсутствуют
deck.show()

# Выводим список карт "в руке"(список hand)
print(hand)