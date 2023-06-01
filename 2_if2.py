"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками.
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры
  и выводя на экран результаты

"""

def main(line1,line2):
    if type(line1) != str or type(line2) != str:
        return 0
    if line1 == line2:
        return 1
    if len(line1) > len(line2):
        return 2
    if line2 == "learn":
        return 3

print (main("привет1", 0))
print (main("привет", "привет"))
print (main("здравствуй", "привет"))
print (main("прива", "learn"))
