"""
Абстрактные классы
Абстрактным называется объявленный, но не реализованный метод.
Абстрактные классы не могут быть инстанциированы, от них нужно унаследовать,
реализовать все их абстрактные методы и только тогда можно создать экземпляр такого класса
"""


from abc import ABC, abstractmethod


class ChessPiece(ABC):
    # общий метод, который будут использовать все наследники этого класса
    def draw(self):
        print("Drew a chess piece")

    # абстрактный метод, который будет необходимо переопределять для каждого подкласса
    @abstractmethod
    def move(self):
        pass

# Попытаемся инстанциировать класс
# a = ChessPiece()

class Queen(ChessPiece):
    def move(self):
        pass

    def move(self):
        print("Moved Queen to e2e4")


# Мы можем создать экземпляр класса
q = Queen()
# # И нам доступны все методы класса
q.draw()
q.move()

