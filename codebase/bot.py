import telebot
from wiki_search import request_to_wiki

bot = telebot.TeleBot('Your token')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "I'm a robot. I don't feel anything. You are not a robot, but can't feel things too")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/help":
        bot.send_message(message.from_user.id, "Write a word or few words to search it in Wikipedia")
        bot.register_next_step_handler(message, search_wiki_handler)
    else:
        bot.send_message(message.from_user.id, "I can't understand you. Write /help.")


@bot.message_handler(content_types=['text'])
def search_wiki_handler(message) -> None:
    if message.text == "/help":
        bot.register_next_step_handler(message, get_text_messages)
    elif message.text == "/start":
        bot.register_next_step_handler(message, send_welcome)

    request_result, flag = request_to_wiki(request=message.text)
    if flag != 'One':
        bot.send_message(message.from_user.id, 'Try choose one option:')
        bot.send_message(message.from_user.id, request_result)
        bot.register_next_step_handler(message, search_wiki_handler)
    else:
        bot.send_message(message.from_user.id, request_result['summary'])
        bot.send_message(message.from_user.id, request_result['link'])
    bot.register_next_step_handler(message, search_wiki_handler)


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=1)