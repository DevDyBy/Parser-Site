import os
import telebot
import wget 
import time

inform = []

bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Отправь мне адресс сайта(https://...). Отправь мне команду /html чтобы скачать HTML (макет) сайта.")

@bot.message_handler(commands=['html'])
def send_html(message):
	wget.download(inform[0], "layout.html")
	time.sleep(3.6)
	file = open('layout.html', 'rb')
	time.sleep(2)
	bot.send_document(message.chat.id, file)
	time.sleep(0.5)
	file.close()
	time.sleep(0.2)
	if os.path.isfile('C:/Users/User/bots/layout.html'):
		os.remove('C:/Users/User/bots/layout.html') 
	else: 
		bot.send_message(message.chat.id, "Ошибка Шрёдингера - она одновренно есть и нет, \nтак же как моя должность джуниор разработчика 😐")
	del inform[0]

@bot.message_handler(content_types=['text'])
def send_adress(message):
	if message.text.startswith('https://') == True:
		inform.append(message.text)
		bot.send_message(message.chat.id, "Теперь отправь команду /html.")

bot.polling()






