import random
import pygame


def build_question():
    kilometer_per_liter = 15
    chosen_distance = 45
    correct_answer = chosen_distance // kilometer_per_liter * 3
    options = [correct_answer, correct_answer - 1, correct_answer + 1, correct_answer + 2]
    random.shuffle(options)

    return {
        "title": "Расход топлива",
        "story": "Автомобиль тратит одинаковое количество топлива на каждый километр.",
        "prompt": f"Если машина проезжает {kilometer_per_liter} км на 3 литра, сколько литров нужно на {chosen_distance} км?",
        "correct_answer": correct_answer,
        "options": options,
        "explanation": "Чем больше путь, тем больше топлива. Это прямая пропорция.",
    }


def draw_scene(screen, title_font, body_font, small_font, width, height, question):
    """Рисуем машину и канистру."""
    pygame.draw.rect(screen, (255, 247, 214), (70, 220, 320, 220), border_radius=20)
    pygame.draw.rect(screen, (0, 0, 0), (70, 220, 320, 220), 3, border_radius=20)

    pygame.draw.rect(screen, (54, 102, 208), (110, 310, 150, 70), border_radius=20)
    pygame.draw.rect(screen, (255, 255, 255), (120, 320, 80, 40), border_radius=12)
    pygame.draw.circle(screen, (20, 20, 20), (150, 380), 18)
    pygame.draw.circle(screen, (20, 20, 20), (230, 380), 18)

    pygame.draw.rect(screen, (229, 115, 115), (300, 310, 80, 50), border_radius=10)
    pygame.draw.rect(screen, (255, 255, 255), (315, 320, 40, 30), border_radius=4)

    fuel_text = small_font.render("Машина", True, (20, 20, 20))
    screen.blit(fuel_text, (470, 305))
