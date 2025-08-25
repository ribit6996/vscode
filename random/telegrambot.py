

bot = telebot('7877167779:AAGoL-it_3nuVyqHFVSVgR-6eLZYs2MLIxw')

@bot.message_hadler(commands=['starrt'])
def main(message):
    bot.send_massage(message.chat.id, 'привет!')

bot.polling(none_stop=True)