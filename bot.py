import telebot
import config

from telebot import types 

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):

  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  item1 = types.KeyboardButton("🌯Menu")
  item2 = types.KeyboardButton("🔄Zacząć od nowa")
  item3 = types.KeyboardButton("🗺Adres")

  markup.add(item1, item2, item3)
 
  bot.send_message(message.chat.id, "Hejka, {0.first_name}!\nJestem <b>SKILL-botem</b>.\nPomogę Ci złożyć zamówienie na SKILLu.".format(message.from_user, bot.get_me()),
      parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
  if message.chat.type == 'private':
    if message.text == '🔄Zacząć od nowa':
      markup = types.InlineKeyboardMarkup(row_width=2)
      item1 = types.InlineKeyboardButton("Tak", callback_data='y')
      item2 = types.InlineKeyboardButton("Nie", callback_data='n')
      markup.add(item1, item2)
      bot.send_message(message.chat.id, 'Napewno chcesz zacząć od nowa?', reply_markup=markup)

    elif message.text == '🗺Adres':
      markup = types.InlineKeyboardMarkup(row_width=1)
      item1 = types.InlineKeyboardButton("Otwórz mapę", callback_data='map')
      markup.add(item1)

      bot.send_message(message.chat.id, 'Jutrzenki 156, 02-226 Warszawa', reply_markup=markup)  

  

# RUN
bot.polling(none_stop=True)
