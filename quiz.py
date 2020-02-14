import os

# Это заглушка, что бы потом можно было спарсить сразу много файлов
PATH = os.path.relpath('quiz-text')
FILES = os.listdir(PATH)
file_name = PATH + '/' + FILES[1]


def get_quiz():
    quiz_params = []
    with open(file_name, 'r', encoding='KOI8-R') as file_text:
        split_text = file_text.read().split('\n\n')
        for block in split_text:
            if "Вопрос" in block or "Ответ" in block:
                quiz_params.append(block.split('\n'))

    questions = [' '.join(question_block[1:]) for question_block in quiz_params if "Вопрос" in question_block[0]]
    answers = [' '.join(answer_block[1:]) for answer_block in quiz_params if "Ответ" in answer_block[0]]
    quiz_questions = dict(zip(questions, answers))

    return quiz_questions


if __name__ == '__main__':
    get_quiz()
