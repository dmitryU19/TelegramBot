import telebot
import config
import db
from telebot import types
from random import randrange

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=["start"])
def cmd_start(message):
    bot.send_message(message.chat.id, config.message_library["start_message"])
    db.set_state(message.chat.id, config.States.S_PERSONAL_DATA_REQUEST.value)
    user_personal_data_permission(message)


@bot.message_handler(commands=["reset"])
def cmd_reset(message):
    bot.send_message(message.chat.id, config.message_library["reset_message"])
    db.set_state(message.chat.id, config.States.S_START.value)


@bot.message_handler(func=lambda message: db.get_current_state(message.chat.id) ==
                                          config.States.S_PERSONAL_DATA_REQUEST.value)
def user_personal_data_permission(message):
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Так', callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Ні', callback_data='no')
    keyboard.add(key_no)
    bot.send_message(message.chat.id,
                     text=config.message_library["personal_data_permission"], reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: db.get_current_state(call.message.chat.id) ==
                                          config.States.S_PERSONAL_DATA_REQUEST.value)
def callback_personal_data(call):
    if call.data == "yes":
        db.set_state(call.message.chat.id, config.States.S_USER_SEARCH.value)
        user_search(call.message)
    elif call.data == "no":
        bot.send_message(call.message.chat.id, config.message_library["personal_data_permission"])
        db.set_state(call.message.chat.id, config.States.S_START.value)


@bot.message_handler(func=lambda message: db.get_current_state(message.chat.id) ==
                                          config.States.S_USER_SEARCH.value)
def user_search(message):
    bot.send_message(message.chat.id, config.message_library["user_found"] % message.chat.username)
    db.set_state(message.chat.id, config.States.S_MAIN_MENU.value)
    bot.send_message(message.chat.id, config.message_library["main_menu"])


@bot.message_handler(func=lambda message: db.get_current_state(message.chat.id) ==
                                          config.States.S_MAIN_MENU.value)
def user_main_menu(message):
    if message.text.isdigit() and message.text == '1':
        db.set_state(message.chat.id, config.States.S_GEO_LOCATION_TYPE.value)
        bot.send_message(message.chat.id, config.message_library["geo_location_type"])
    else:
        bot.send_message(message.chat.id, config.message_library["unknown_command"])


@bot.message_handler(func=lambda message: db.get_current_state(message.chat.id) ==
                                          config.States.S_GEO_LOCATION_TYPE.value)
def user_geo_location_type(message):
    if message.content_type == 'text' or message.content_type == 'location':
        db.set_state(message.chat.id, config.States.S_TROUBLE_LOCATION_ANSWER.value)
        keyboard = types.InlineKeyboardMarkup()
        key_outdoor = types.InlineKeyboardButton(text='На вулиці', callback_data='outdoor')
        keyboard.add(key_outdoor)
        key_indoor = types.InlineKeyboardButton(text='В приміщенні', callback_data='indoor')
        keyboard.add(key_indoor)
        bot.send_message(message.chat.id,
                         text=config.message_library["trouble_place"], reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, config.message_library["unknown_type"])


@bot.callback_query_handler(func=lambda call: db.get_current_state(call.message.chat.id) ==
                                          config.States.S_TROUBLE_LOCATION_ANSWER.value)
def callback_location(call):
    if call.data == "outdoor":
        db.set_state(call.message.chat.id, config.States.S_TROUBLE_TYPE.value)
        trouble_type(call.message)
    elif call.data == "indoor":
        db.set_state(call.message.chat.id, config.States.S_TROUBLE_LOCATION_INDOOR.value)
        bot.send_message(call.message.chat.id, config.message_library["location_floor"])


@bot.message_handler(func=lambda message: db.get_current_state(message.chat.id) ==
                                          config.States.S_TROUBLE_LOCATION_INDOOR.value)
def user_location_floor(message):
    if message.text.isdigit():
        db.set_state(message.chat.id, config.States.S_TROUBLE_TYPE.value)
        trouble_type(message)
    else:
        bot.send_message(message.chat.id, config.message_library["unknown_floor"])


def trouble_type(message):
    keyboard = types.InlineKeyboardMarkup()
    key_voice = types.InlineKeyboardButton(text='Голос', callback_data='voice')
    keyboard.add(key_voice)
    key_data = types.InlineKeyboardButton(text='Дані', callback_data='data')
    keyboard.add(key_data)
    bot.send_message(message.chat.id,
                     text=config.message_library["trouble_type"], reply_markup=keyboard)
    db.set_state(message.chat.id, config.States.S_TROUBLE_TYPE_ANSWER.value)


@bot.callback_query_handler(func=lambda call: db.get_current_state(call.message.chat.id) ==
                                          config.States.S_TROUBLE_TYPE_ANSWER.value)
def callback_trouble_type(call):
    if call.data == "voice":
        db.set_state(call.message.chat.id, config.States.S_NETWORK_TYPE.value)
        keyboard = types.InlineKeyboardMarkup()
        key_2g = types.InlineKeyboardButton(text='2G', callback_data='2g')
        keyboard.add(key_2g)
        key_3g = types.InlineKeyboardButton(text='3G', callback_data='3g')
        keyboard.add(key_3g)
        key_skip = types.InlineKeyboardButton(text='Пропустити', callback_data='skip')
        keyboard.add(key_skip)
        bot.send_message(call.message.chat.id,
                         text=config.message_library["network_type"], reply_markup=keyboard)
    elif call.data == "data":
        db.set_state(call.message.chat.id, config.States.S_NETWORK_TYPE.value)
        keyboard = types.InlineKeyboardMarkup()
        key_2g = types.InlineKeyboardButton(text='2G', callback_data='2g')
        keyboard.add(key_2g)
        key_3g = types.InlineKeyboardButton(text='3G', callback_data='3g')
        keyboard.add(key_3g)
        key_4g = types.InlineKeyboardButton(text='4G', callback_data='4g')
        keyboard.add(key_4g)
        key_skip = types.InlineKeyboardButton(text='Пропустити', callback_data='skip')
        keyboard.add(key_skip)
        bot.send_message(call.message.chat.id,
                         text=config.message_library["network_type"], reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: db.get_current_state(call.message.chat.id) ==
                                          config.States.S_NETWORK_TYPE.value)
def callback_network_type(call):
    if call.data == "2g" or call.data == "3g" or call.data == "4g" or call.data == "skip":
        db.set_state(call.message.chat.id, config.States.S_TICKET_NUMBER.value)
        bot.send_message(call.message.chat.id, config.message_library["ticket_number"] % str(randrange(100, 200)))


bot.polling()
