import random
import pygame


def build_question():
    money_per_customer = 50
    chosen_customers = 30
    correct_answer = money_per_customer * chosen_customers
    options = [correct_answer, correct_answer - 100, correct_answer + 100, correct_answer + 200]
    random.shuffle(options)

    return {
        "title": "Выручка магазина",
        "story": "Каждый покупатель приносит одинаковую сумму в магазин.",
        "prompt": f"Если 1 покупатель приносит {money_per_customer} монет, сколько монет принесут {chosen_customers} покупателей?",
        "correct_answer": correct_answer,
        "options": options,
        "explanation": "Больше покупателей — больше выручка. Это прямая пропорция.",
    }


def draw_scene(screen, title_font, body_font, small_font, width, height, question):
    """Рисуем магазин и покупателей."""
    pygame.draw.rect(screen, (255, 247, 214), (70, 220, 320, 220), border_radius=20)
    pygame.draw.rect(screen, (0, 0, 0), (70, 220, 320, 220), 3, border_radius=20)

    pygame.draw.rect(screen, (54, 102, 208), (120, 260, 140, 120), border_radius=12)
    pygame.draw.rect(screen, (255, 255, 255), (140, 280, 100, 80), border_radius=8)
    for x in [120, 220, 320]:
        pygame.draw.circle(screen, (255, 159, 67), (x, 330), 24)

    shop_text = small_font.render("Магазин", True, (20, 20, 20))
    screen.blit(shop_text, (470, 305))
