
class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


inp_data = input("Введите положительное число: ")

try:
    inp_data = int(inp_data)
    if inp_data < 0:
        raise OwnError("Вы ввели отрицательное число!")
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print(f"Все хорошо. Ваше число: {inp_data}")


class MyError(Exception):

    # Конструктор или инициализатор
    def __init__(self, value):
        self.value = value

    # __str__ должен напечатать () значение
    def __str__(self):
        return (repr(self.value))


try:
    raise(MyError(3 * 2))

# Значение исключения хранится в ошибке
except MyError as error:
    print('A New Exception occured: ', error.value)