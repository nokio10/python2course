import random


class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        """  Подбрасывание монетки """
        self.side = random.randint(0, 1)
        # return side # Это ошибка, здесь return не нужен


# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
# Выведите соотношение выпавших орлов и решек в процентах

# Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
# не выпала ни орлом ни решкой. Монетка "определяется" со стороной(орел/решка),
# только после того, как вы ее подбрасываете(вызываете метод flip())


n = int(input('Введите количество монет: '))
coins = [Coin() for i in range(n)]
for coin in coins:
    coin.flip()  # Подбрасывание каждой монетки
heads_count = []
for coin in coins:
    if coin.side == 0:
        heads_count.append(coin)
tails_count = n - len(heads_count)
print(len(heads_count))
print(f'Соотношение выпавших орлов: {len(heads_count) / n * 100}%')
print(f'Соотношение выпавших решек: {tails_count / n * 100}%')
