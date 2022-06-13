# -*- coding: utf-8 -*-

# Код со времён мамонтов, не удивляйтесь если найдете говнокод
# Так-то, это мой первый бот в телеграме написаный на питоне

import telebot
from telebot import types

bot = telebot.TeleBot('token') # токен бота

@bot.message_handler(commands = ['support'])
def support(message):
	inline_about = types.InlineKeyboardMarkup()
	telegram_link = types.InlineKeyboardButton(text="Основной канал Telegram", url="https://t.me/protectcheck")
	telegram_chat = types.InlineKeyboardButton(text="Telegram-чат", url="https://t.me/joinchat/Lmw4zBe7JEo2MDJi")
	ds_server = types.InlineKeyboardButton(text="Дискорд-сервер", url="https://discord.gg/usZfpTtQk8")
	yt = types.InlineKeyboardButton(text="Ютуб-канал", url="https://www.youtube.com/channel/UCppLVrmDsi4cQTTilUFvgqg")
	oth = types.InlineKeyboardButton(text="Доп. телеграм-канал", url="https://t.me/crashbotsdiscord")
	inline_about.row(telegram_link)
	inline_about.row(telegram_chat)
	inline_about.row(ds_server)
	inline_about.row(yt)
	inline_about.row(oth)
	bot.send_message(message.from_user.id, "Поддержка", reply_markup = inline_about)

@bot.message_handler(commands = ['bots'])
def bots(message):
	inline_about = types.InlineKeyboardMarkup()
	antilavan = types.InlineKeyboardButton(text="Anti-Lavan", url="https://t.me/crashbotsdiscord/5")
	mee6 = types.InlineKeyboardButton(text="MEE6 For Developers", url="https://discord.com/api/oauth2/authorize?client_id=896647507336114187&permissions=8&scope=bot")
	anonymous = types.InlineKeyboardButton(text="Anonymous BOT", url="https://discord.com/api/oauth2/authorize?client_id=896653080748261446&permissions=8&scope=bot")
	vc = types.InlineKeyboardButton(text="Voice BOT", url="https://discord.com/api/oauth2/authorize?client_id=896657069506183218&permissions=8&scope=bot")
	chaos = types.InlineKeyboardButton(text="Chaos BOT", url="https://discord.com/api/oauth2/authorize?client_id=896657926155038740&permissions=8&scope=bot")
	inline_about.row(antilavan)
	inline_about.row(mee6)
	inline_about.row(anonymous) # Да-да, до for _ in ... я не догадался
	inline_about.row(vc)
	inline_about.row(chaos)
	bot.send_message(message.from_user.id, "Краш-боты\nВыбери нужного тебе бота:", reply_markup = inline_about)


@bot.message_handler(commands = ['guide'])
def guidee(message):
	bot.send_message(message.from_user.id, "Гайд по краш-ботам\nЧтобы посмотреть список всех доступных краш ботов, напишите /bots \n\nMEE6 For Developers - классический краш-бот.\nДля получения списка команд добавьте бота на сервер по ссылке из команды /bots и пропишите !help\n\nAnonymous BOT - стандартный краш-бот.\nКрашит командой !go\n\nVoice BOT - автоматический Краш-бот.\nКрашит сервер автоматически при добавлении на сервер\n\nChaos BOT - легенда 2020 года. Классический краш-бот.\nЭтот бот не является оригинальным Chaos-ом, но это хорошая подделка.\nСписок команд можно получить командой !helpchaos\n\nAnti-Lavan - обход анти-краш-ботов\nОбходит лавана, и некоторых анти-краш-ботов. \nИнструкция - https://youtu.be/w_WAW5sCRdI")

@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.from_user.id, "Привет! Я бот дискорд-сервера Frzl Support, и я буду рад тебе помочь!\n/support - актуальные ссылки для получения тех.поддежки/связи с создателем\n/bots - получить ссылки на краш ботов\n/guide - гайд по всем краш ботам")

@bot.message_handler(commands=['help'])
def hlp(message):
	bot.send_message(message.from_user.id, "Привет! Я бот дискорд-сервера Frzl Support, и я буду рад тебе помочь!\n/support - актуальные ссылки для получения тех.поддежки/связи с создателем\n/bots - получить ссылки на краш ботов\n/guide - гайд по всем краш ботам")

bot.polling(none_stop=True, interval=0)
