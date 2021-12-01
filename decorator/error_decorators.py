
def error_wrapper(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except ZeroDivisionError:
            print("Деление на ноль!")
        except TypeError:
            print("Неверный тип входных данных!")
    return wrapper


@error_wrapper
def division(a, b):
    print(a/b)

division(1, 3)
