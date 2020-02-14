import os
import random
from quiz_text import get_quiz
import logging
from dotenv import load_dotenv
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
import redis

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

NEW_QUESTION_REQUEST, SOLUTION_ATTEMPT = range(2)

load_dotenv()
redis_password = os.getenv('REDIS_PASSWORD')
redis_port = os.getenv('REDIS_PORT')
redis_host = os.getenv('REDIS_HOST')

r = redis.Redis(host=redis_host, port=redis_port,
                    password=redis_password)


def start(update, context):
    custom_keyboard = [['Новый вопрос', 'Сдаться'], ['Мой счёт']]
    update.message.reply_text(
        'Привет! Я бот для викторин!',
        reply_markup=telegram.ReplyKeyboardMarkup(custom_keyboard)
    )

    return NEW_QUESTION_REQUEST


def handle_new_question_request(update, context):
    if update.message.text == 'Новый вопрос':
        random_number = random.randint(0, len(get_quiz()) - 1)
        random_question = list(get_quiz().keys())[random_number]
        context.bot.send_message(chat_id=update.message.chat_id, text=random_question)
        r.set(update.message.chat_id, random_question)

    return SOLUTION_ATTEMPT


def handle_solution_attempt(update, context):
    chat_id = update.message.chat_id
    question = r.get(chat_id)
    answer = get_quiz()[question.decode('utf-8')]
    if answer == update.message.text:
        update.message.reply_text('Правильно! Поздравляю! Для следующего вопроса нажми «Новый вопрос»')
        return NEW_QUESTION_REQUEST
    else:
        update.message.reply_text('Неправильно... Попробуешь ещё раз?')


def handle_give_up(update, context):
    if update.message.text == 'Сдаться':
        chat_id = update.message.chat_id
        question = r.get(chat_id)
        answer = get_quiz()[question.decode('utf-8')]
        update.message.reply_text(answer)

    random_number = random.randint(0, len(get_quiz()) - 1)
    random_question = list(get_quiz().keys())[random_number]
    context.bot.send_message(chat_id=update.message.chat_id, text=random_question)
    r.set(update.message.chat_id, random_question)

    return SOLUTION_ATTEMPT


def end(update, context):
    update.message.reply_text('До свидания, надеюсь тебе понравилась игра!',
                              reply_markup=telegram.ReplyKeyboardRemove())

    return ConversationHandler.END


def main():
    telegram_token = os.getenv('TELEGRAM_ACCESS_TOKEN')
    update = Updater(telegram_token, use_context=True)
    dp = update.dispatcher
    quiz_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            NEW_QUESTION_REQUEST: [
                MessageHandler(Filters.regex('^(Новый вопрос|Сдаться|Мой счёт)$'), handle_new_question_request)
            ],
            SOLUTION_ATTEMPT: [
                MessageHandler(Filters.regex('^(Сдаться)$'), handle_give_up),
                MessageHandler(Filters.text, handle_solution_attempt)
            ],
        },
        fallbacks=[CommandHandler('end', end)]
    )

    dp.add_handler(quiz_handler)
    update.start_polling()
    update.idle()


if __name__ == '__main__':
    main()
