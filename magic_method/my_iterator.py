class Iterator:
    """
    Объект-итератор
    """
    def __init__(self, start=0):
        self.i = start-1
    # У итератора есть метод __next__

    def __next__(self):
        self.i += 1
        if self.i <= 5:
            return self.i
        else:
            raise StopIteration

    def __iter__(self):
        return self


obj = Iterator(start=1)
for el in obj:
    print(el)
