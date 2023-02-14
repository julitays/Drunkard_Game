                                                        # Проверка знаний ООП и создание карточной игры: "Пьяница"
from random import shuffle
class Card:
    suits = ['пикей', 'бубей', 'червей', 'крестей']     # Масти, которые могут быть у выпавших карт
    values = [None, None, 'Двойка', 'Тройка', 'Четверка',
              'Пятерка', 'Шестерка', 'Семёрка', 'Восьмёрка',
              'Девятка', 'Десятка', 'Валет', 'Дама',
              'Король', 'Туз']                         ## Различные номиналы карт, два None нужны для правильной
                                                        ## индексации, таким образом карта 2 на 2-ом индексе в списке

    def __init__(self, v, s):                           # Переменные одного экземпляра, создают вид карты объекта
        """Suits and values - это целые числа"""
        self.value = v
        self.suit = s

    def __it__(self, c2):

        if self.value < c2.value:
            return True                                 ## Самая сильная масть располагается последней, то есть она
                                                        ## назначена наибольшему индексу, а самая слабая масть
                                                        ## назначена наименьшему индексу.

        if self.value == c2.value:                      # В таком случае методы используют масти, чтобы избежать ничьей.
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):

        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            return False
        return False

    def __repr__(self):
        v = self.values[self.value] + ' ' + self.suits[self.suit] # Выводит карту по названию переменных
        return v


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):                  # Первое значение для карты — это 2, а последнее — 14 (туз).
            for j in range(4):                  # Так создаются 52 карты, по карте на каждую комбинацию масти и значения.
                self.cards.append(Card(i, j))
        shuffle(self.cards)                     # Имитируем перетасовку колоды карт.

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

# deck = Deck()
# for card in deck.cards:
#     print(card)

class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0                           # для отслеживания количества раундов, выигранных игроком
        self.card = None                        # для представления карты, которую в данный момент держит игрок;
