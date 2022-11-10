import telebot
from telebot import types

bot = telebot.TeleBot('5490555803:AAHaSCIWAKI2daODJj43wGxZhteSZc5oZIU')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Здравствуй, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>, Eсть всего 3 функции:\n1) /photo (отправляешь фото, получаешь оценку)\n2) /website (Отправлят ссылку на <b>Youtube</b>)\n3) /help (Кнопки первый двух функций)'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Классное фото)')

# Отправляет ссылку на Youtube
@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Посетить веб сайт', url='https://www.youtube.com'))
    bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)

@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton('/website')
    start = types.KeyboardButton('/start')
    markup.add(website, start)
    bot.send_message(message.chat.id, 'Выбирай', reply_markup=markup)


bot.polling(none_stop=True)
