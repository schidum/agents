import pygame


def make_options(correct_answer):
    """Создаём два похожих ошибочных варианта и перемешиваем их."""
    options = [correct_answer]
    if correct_answer - 10 >= 1:
        options.append(correct_answer - 10)
    else:
        options.append(correct_answer + 5)

    if correct_answer + 10 not in options:
        options.append(correct_answer + 10)
    else:
        options.append(correct_answer + 5)

    if correct_answer + 20 not in options:
        options.append(correct_answer + 20)
    else:
        options.append(correct_answer + 15)

    options = list(dict.fromkeys(options))
    pygame.random.shuffle(options)
    return options
