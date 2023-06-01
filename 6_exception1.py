"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она
  перехватывала KeyboardInterrupt, писала пользователю "Пока!"
  и завершала работу при помощи оператора break

"""

def hello_user():
    try:
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
    except KeyboardInterrupt:
        print("Пока!")

hello_user()
