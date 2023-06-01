"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает
  пользователя “Как дела?”, пока он не ответит “Хорошо”

"""

def hello_user():
    first_question = True
    while True:
        if first_question:
            user_say = input('Как дела? ')
            first_question = False
        else:
            user_say = input('А если подумать? ')
        if user_say == 'Хорошо':
            print('Ок')
            break

hello_user()
