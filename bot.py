from telebot import TeleBot,types
from config import bot_token
from pwd_ghenerator import *

bot = TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет, я помогу тебе с генерацией и хранением паролей")


@bot.message_handler(commands=['gen_pwd'])
def gen_pwd(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(types.KeyboardButton("1"))
    keyboard.add(types.KeyboardButton("2"))
    keyboard.add(types.KeyboardButton("3"))
    keyboard.add(types.KeyboardButton("4"))
    bot.send_message(message.chat.id, "Выберите сложность пароля", reply_markup=keyboard)
    bot.register_next_step_handler(message, get_level)
    
def get_level(message):
    global passw
    if message.text == "1":
        passw = gen_passwd(symbols=False, upper=False)
    if message.text == "2":
        passw = gen_passwd(len=12, symbols=False)
    if message.text == "3":
        passw = gen_passwd(len=15)
    if message.text == "4":
        passw = gen_passwd(len=20)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(types.KeyboardButton("Сохранить пароль"))
    keyboard.add(types.KeyboardButton("Сгенерировать новый пароль"))
    bot.send_message(message.chat.id, passw, reply_markup=keyboard)
    bot.register_next_step_handler(message, save_password)
    
def save_password(message):
    if message.text == "Сохранить пароль":
        bot.send_message(message.chat.id, "Напиши логин и адрес сайта через пробел")
        bot.register_next_step_handler(message, save_password_handler)
    if message.text == "Сгенерировать новый пароль":
        gen_pwd(message)

def save_password_handler(message):
    login, site = message.text.split(" ")
    saved_passwords_to_file(login,passw, site)
    bot.send_message(message.chat.id, "Пароль успешно сохранен")

bot.infinity_polling()