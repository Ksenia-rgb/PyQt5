import requests
import json
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

URL_CAT = 'https://cataas.com/cat'
URL_DOG = 'https://random.dog/woof.json'
URL_BORED = 'http://www.boredapi.com/api/activity/'
TOKEN = '5925362190:AAGhjITTcABGKa08EODzdPfcjpWlzE8frTc'

bot = telebot.TeleBot(TOKEN)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton('Котика!'))
keyboard.add(KeyboardButton('Пёсика!'))
keyboard.add(KeyboardButton('Об авторе'))
keyboard.add(KeyboardButton('Мне скучно'))


def get_cat():
    response = requests.get(URL_CAT)
    return response.content


def get_dog():
    response = requests.get(URL_DOG)
    return response.content


def get_bored():
    response = requests.get(URL_BORED)
    return response.content


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Я тестовый бот!', reply_markup=keyboard)


@bot.message_handler(regexp='кот')
def cat_picture(message):
    photo = get_cat()
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(regexp='пёс')
def dog_picture(message):
    photo = get_dog()
    bot.send_message(message.chat.id, photo)


@bot.message_handler(regexp='автор')
def author_info(message):
    info = 'Автор очень любит котиков и пёсиков'
    bot.send_message(message.chat.id, info)


@bot.message_handler(regexp='скучно')
def bored_info(message):
    info = get_bored()
    info1 = json.loads(info.decode('utf-8'))
    bot.send_message(message.chat.id, info1['activity'])


bot.infinity_polling()