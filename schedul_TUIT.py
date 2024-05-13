import pandas as pd
import telebot
from telebot import types
from telegram import InlineKeyboardMarkup
import config


bot = telebot.TeleBot(config.token)


def load_orders():
    excel_files = "/media/dauletiyar/F044C97A44C943D6/Users/daule/Documents/Dauletiyar/Репик/Python/Projects/telegram bots/Sirtqi_3-kurs dars jadval.xlsx"
    sheets_name = "010-011-21"
    df = pd.read_excel(excel_files, sheets_name=sheets_name)
    df["Nomer zakaza"] = df["Nomer zakaza"].astype(str)
    return df


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1_1 = types.KeyboardButton("1")
    btn2_2 = types.KeyboardButton("2")
    btn3_3 = types.KeyboardButton("3")
    btn4_4 = types.KeyboardButton("4")
    markup.add(btn1_1, btn2_2, btn3_3, btn4_4)
    bot.send_message(message.chat.id, f'Здравствуйте {message.from_user.first_name} выберите курс: ', reply_markup=markup)

@bot.message_handler(commands=['help'])
def main(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("/week")
    btn2 = types.KeyboardButton("/today")
    btn3 = types.KeyboardButton("/tomorrow")
    btn4 = types.KeyboardButton("/start")
    btn5 = types.KeyboardButton("/help")
    btn6 = types.KeyboardButton("/info")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    bot.send_message(message.chat.id, "Бот для расписания уроков ТУИТ.\n"
                                      "/today - Посмотреть расписание занятий на сегодня.\n"
                                      "/tomorrow - Расписание уроков завтрашнего дня.\n"
                                      "/week - Целая неделя.\n"
                                      "/start - Чтобы изменить группу \n"
                                      "Если вы видите сообщение 'This message is not supported', вам необходимо обновить версию Telegram", reply_markup=markup)

@bot.message_handler(commands=['time'])
def main(message):
    bot.send_message(message.chat.id, "1-смена: (1,2,3 курсы)\n"
                                      "1-пара: 08:30 – 09:50\n"
                                      "2-пара: 10:00 – 11:20\n"
                                      "3-пара: 11:30 – 12:50\n"
                                      "4-пара: 13:30 – 14:50\n""\n"
                                      "2-смена (4 курсы):\n"
                                      "1-пара: 13:30 – 14:50\n"
                                      "2-пара: 15:00 – 16:20\n"
                                      "3-пара: 16:30 – 17:50\n"
                                      "4-пара: 18:00 – 19:20")

@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, "Автор: Калилаев Даулетияр (dauletiyar03@gmail.com)")

@bot.message_handler(commands=['today'])
def today(message):
    bot.send_message(message.chat.id, "у вас сегодня нет паров")

# bot.polling(non_stop=True)
bot.infinity_polling()