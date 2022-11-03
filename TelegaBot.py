import telebot

bot = telebot.TeleBot('5490555803:AAHaSCIWAKI2daODJj43wGxZhteSZc5oZIU')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Здарова')

bot.polling(none_stop=True)