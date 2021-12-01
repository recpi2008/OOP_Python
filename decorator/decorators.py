"""
Декораторы

Декоратор — это функция, которая позволяет обернуть другую функцию
для расширения её функциональности без непосредственного изменения её кода.
"""

#
# def wrapper_function():
#     def hello_world():
#         print('Hello world!')
#     hello_world()
#
#
# wrapper_function()


def higher_order(func):
    print('Получена функция {} в качестве аргумента'.format(func))
    func()
    return func


# def decorator_function(func):
#     def wrapper():
#         print('Функция-обёртка!')
#         print('Оборачиваемая функция: {}'.format(func))
#         print('Выполняем обёрнутую функцию...')
#         func()
#         print('Выходим из обёртки')
#     return wrapper
#
#
# @decorator_function
# def hello_world():
#     print('Hello world!')
#
#
# hello_world()



