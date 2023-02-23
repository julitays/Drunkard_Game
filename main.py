# Проверка знаний ООП и создание карточной игры: "Пьяница"
from random import shuffle


class Card:
    suits = ['пикей', 'бубей', 'червей', 'крестей']  # Масти, которые могут быть у выпавших карт
    values = [None, None, 'Двойка', 'Тройка', 'Четверка',
              'Пятерка', 'Шестерка', 'Семёрка', 'Восьмёрка',
              'Девятка', 'Десятка', 'Валет', 'Дама',
              'Король', 'Туз']  ## Различные номиналы карт, два None нужны для правильной

    ## индексации, таким образом карта 2 на 2-ом индексе в списке

    def __init__(self, v, s):  # Переменные одного экземпляра, создают вид карты объекта
        """Suits and values - это целые числа"""
        self.value = v
        self.suit = s

    def __it__(self, c2):

        if self.value < c2.value:
            return True  ## Самая сильная масть располагается последней, то есть она
            ## назначена наибольшему индексу, а самая слабая масть
            ## назначена наименьшему индексу.

        if self.value == c2.value:  # В таком случае методы используют масти, чтобы избежать ничьей.
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
        v = self.values[self.value] + ' ' + self.suits[self.suit]  # Выводит карту по названию переменных
        return v


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):  # Первое значение для карты — это 2, а последнее — 14 (туз).
            for j in range(4):  # Так создаются 52 карты, по карте на каждую комбинацию масти и значения.
                self.cards.append(Card(i, j))
        shuffle(self.cards)  # Имитируем перетасовку колоды карт.

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
        self.wins = 0  # для отслеживания количества раундов, выигранных игроком
        self.card = None  # для представления карты, которую в данный момент держит игрок;


class Game:
    def __init__(self):
        name1 = input('Имя игрока 1: ')
        name2 = input('Имя игрока 2: ')
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        w = '{} забирает карты'
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} кладет {}, а {} кладет {}"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print('Поехали!')
        while len(cards) >= 2:
            m = "Нажмите X для выхода. Нажмите любую другую клавишу для начала игры. "
            response = input(m)
            if response == 'X' or response == 'x':
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2)
        print('Игра окончена! {} выиграл!'.format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "Ничья!"


game = Game()
game.play_game()
