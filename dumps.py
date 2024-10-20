import telebot

botF = telebot.TeleBot('7799964843:AAGgp_mMQzNFJX2gDLISHSGhGBtSypXvjY4')
# botF.send_message(2338015635, 'test')


@botF.message_handler(func=lambda message: True)
def echo_all(message):
    print(message.chat.id)  # Печатает ID чата
    botF.send_message(-1002338015635, 'test')

# Запуск бота
botF.polling()