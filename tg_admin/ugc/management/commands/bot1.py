import telebot
from telebot import types


TOKEN = "1878942323:AAEP9vKSwIqSXAWBmEDvZ3UwZMHUgnNCmXk"

bot = telebot.TeleBot(TOKEN, threaded=False)


@bot.message_handler(commands=['start'])
def command_start(message):
    
	start_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
	start_markup.row('/start', '/help','/hide')
	start_markup.row('/get_started','/otcuda_cash', '/calculat')
	start_markup.row('/static', '/registration','/agreement')
	bot.send_message(message.chat.id, f"👋 Привет, {message.from_user.first_name}! 👋")
	bot.send_message(message.from_user.id, "⌨️ Клавиатура добалена, нажми раскрыть, \nили \n⌨️ /hide -удалить клавиатуру ", reply_markup=start_markup)
    


print('start')
#if __name__ == "__main__":
bot.polling(none_stop = True)
