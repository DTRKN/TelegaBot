import telebot

bot = telebot.TeleBot('5490555803:AAHaSCIWAKI2daODJj43wGxZhteSZc5oZIU')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, 'Здарова')

bot.polling(none_stop=True)