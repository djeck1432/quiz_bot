import os
import vk_api
import random
import redis
from quiz_text import get_quiz
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from dotenv import load_dotenv


def get_new_question(event, vk, keyboard, r):
    random_question = random.choice(list(get_quiz().keys()))
    vk.messages.send(
        user_id=event.user_id,
        random_id=get_random_id(),
        keyboard=keyboard.get_keyboard(),
        message=random_question
    )
    r.set(event.user_id, random_question)


def get_solution_attempt(event, vk, keyboard, r):
    user_id = event.user_id
    question = r.get(user_id)
    answer = get_quiz()[question.decode('utf-8')]
    if answer == event.text:
        vk.messages.send(
            user_id=event.user_id,
            random_id=get_random_id(),
            keyboard=keyboard.get_keyboard(),
            message='Правильно! Поздравляю! Для следующего вопроса нажми «Новый вопрос»',
        )
    else:
        vk.messages.send(
            user_id=event.user_id,
            random_id=get_random_id(),
            keyboard=keyboard.get_keyboard(),
            message='Неправильно... Попробуешь ещё раз?'
        )


def give_up(event, vk, keyboard, r):
    user_id = event.user_id
    question = r.get(user_id)
    answer = get_quiz()[question.decode('utf-8')]
    vk.messages.send(
        user_id=event.user_id,
        random_id=get_random_id(),
        keyboard=keyboard.get_keyboard(),
        message=answer
    )
    get_new_question(event, vk, keyboard, r)


def main():
    load_dotenv()
    vk_token = os.getenv('VK_ACCESS_TOKEN')
    vk_session = vk_api.VkApi(token=vk_token)
    vk = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)

    redis_password = os.getenv('REDIS_PASSWORD')
    redis_port = os.getenv('REDIS_PORT')
    redis_host = os.getenv('REDIS_HOST')
    r = redis.Redis(host=redis_host, port=redis_port,
                    password=redis_password)

    keyboard = VkKeyboard()
    keyboard.add_button('Новый вопрос', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_button('Сдаться', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Мой счёт')

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            if event.text == 'Новый вопрос':
                get_new_question(event, vk, keyboard, r)
            elif event.text == 'Сдаться':
                give_up(event, vk, keyboard, r)
            else:
                get_solution_attempt(event, vk, keyboard, r)


if __name__ == '__main__':
    main()
