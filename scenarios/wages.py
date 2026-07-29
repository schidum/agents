import random
import pygame


def build_question():
    hours = 2
    money_per_hour = 40
    chosen_hours = 6
    correct_answer = money_per_hour * chosen_hours
    options = [correct_answer, correct_answer - 40, correct_answer + 40, correct_answer + 80]
    random.shuffle(options)

    return {
        "title": "Заработок рабочего",
        "story": "Рабочий получает одинаковую оплату за каждый час работы.",
        "prompt": f"Если он за {hours} часа получает {money_per_hour * hours} монет, сколько он получит за {chosen_hours} часов?",
        "formula_text": f"{money_per_hour} x {chosen_hours} = {correct_answer}",
        "correct_answer": correct_answer,
        "options": options,
        "explanation": "Чем больше часов, тем больше заработок. Это прямая пропорция.",
    }


def draw_scene(screen, title_font, body_font, small_font, width, height, question):
    """Рисуем рабочего, часы и монеты."""
    pygame.draw.rect(screen, (255, 247, 214), (70, 220, 300, 220), border_radius=20)
    pygame.draw.rect(screen, (0, 0, 0), (70, 220, 300, 220), 3, border_radius=20)

    pygame.draw.circle(screen, (240, 190, 90), (170, 290), 36)
    pygame.draw.rect(screen, (100, 100, 100), (140, 325, 60, 90), border_radius=10)
    pygame.draw.rect(screen, (52, 152, 219), (145, 280, 50, 45), border_radius=10)
    pygame.draw.rect(screen, (255, 159, 67), (125, 370, 90, 20), border_radius=8)

    pygame.draw.circle(screen, (255, 215, 0), (430, 270), 24)
    pygame.draw.circle(screen, (255, 215, 0), (470, 270), 24)
    pygame.draw.circle(screen, (255, 215, 0), (510, 270), 24)

    clock_text = small_font.render("Часы", True, (20, 20, 20))
    screen.blit(clock_text, (430, 305))
