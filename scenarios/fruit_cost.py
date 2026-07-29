import random
import pygame


def build_question():
    price_for_two = 100
    chosen_weight = 5
    correct_answer = price_for_two * (chosen_weight // 2)
    options = [correct_answer, correct_answer - 25, correct_answer + 25, correct_answer + 50]
    random.shuffle(options)

    return {
        "title": "Цена фруктов",
        "story": "Каждый килограмм яблок стоит одинаково.",
        "prompt": f"Если 2 кг яблок стоят {price_for_two} монет, сколько стоят {chosen_weight} кг?",
        "formula_text": f"{price_for_two} ÷ 2 x {chosen_weight} = {correct_answer}",
        "correct_answer": correct_answer,
        "options": options,
        "explanation": "Чем больше яблок, тем больше цена. Это прямая пропорция.",
    }


def draw_scene(screen, title_font, body_font, small_font, width, height, question):
    """Рисуем корзину и яблоки."""
    pygame.draw.rect(screen, (255, 247, 214), (70, 220, 320, 220), border_radius=20)
    pygame.draw.rect(screen, (0, 0, 0), (70, 220, 320, 220), 3, border_radius=20)

    pygame.draw.rect(screen, (255, 159, 67), (120, 320, 140, 80), border_radius=14)
    pygame.draw.rect(screen, (229, 115, 115), (140, 280, 100, 40), border_radius=10)
    for x in [115, 165, 215]:
        pygame.draw.circle(screen, (76, 175, 80), (x, 345), 20)
        pygame.draw.circle(screen, (20, 20, 20), (x, 345), 20, 2)

    pygame.draw.circle(screen, (255, 215, 0), (470, 270), 24)
    pygame.draw.circle(screen, (255, 215, 0), (510, 270), 24)
    pygame.draw.circle(screen, (255, 215, 0), (550, 270), 24)

    basket_text = small_font.render("Корзина", True, (20, 20, 20))
    screen.blit(basket_text, (470, 305))
