"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""

import ephem
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')



def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

def where_planet_was (update, context):
    items = update.message.text.split()

    planet = None

    for item in items:
        if item in planets:

            if item == 'Mercury':
                planet = ephem.Mercury
            elif item == 'Earth':
                planet = ephem.Earth
            elif item == 'Mars':
                planet = ephem.Mars
            elif item == 'Jupiter':
                planet = ephem.Jupiter
            elif item == 'Saturn':
                planet = ephem.Saturn
            elif item == 'Uranus':
                planet = ephem.Uranus
            elif item == 'Neptune':
                planet = ephem.Neptune

    date = ephem.Date(items[2])

    if planet is not None:
        result = ephem.constellation(planet(date))
        update.message.reply_text(result)
    else:
        update.message.reply_text('Пожалуйста, укажите название планеты на английском и дату в формате "Planet yyyy/mm/dd" после команды /planet, чтобы посмотреть в каком созвездии она находилась')


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(text)


def main():
    mybot = Updater(settings.API_KEY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_info))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
