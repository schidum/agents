import random
import pygame


def build_question():
    harvest_per_plot = 10
    chosen_plots = 5
    correct_answer = harvest_per_plot * chosen_plots
    options = [correct_answer, correct_answer - 10, correct_answer + 10, correct_answer + 20]
    random.shuffle(options)

    return {
        "title": "Урожай на поле",
        "story": "Каждый участок земли даёт одинаковый урожай.",
        "prompt": f"Если 1 участок даёт {harvest_per_plot} кг, сколько кг даст {chosen_plots} участков?",
        "formula_text": f"{harvest_per_plot} x {chosen_plots} = {correct_answer}",
        "correct_answer": correct_answer,
        "options": options,
        "explanation": "Больше поля — больше урожай. Это прямая пропорция.",
    }


def draw_scene(screen, title_font, body_font, small_font, width, height, question):
    """Рисуем поле и растения."""
    pygame.draw.rect(screen, (255, 247, 214), (70, 220, 320, 220), border_radius=20)
    pygame.draw.rect(screen, (0, 0, 0), (70, 220, 320, 220), 3, border_radius=20)

    pygame.draw.rect(screen, (76, 175, 80), (110, 300, 220, 80), border_radius=8)
    for x in [130, 190, 250]:
        pygame.draw.rect(screen, (255, 215, 0), (x, 280, 10, 40), border_radius=4)
        pygame.draw.circle(screen, (76, 175, 80), (x + 6, 270), 16)

    field_text = small_font.render("Поле", True, (20, 20, 20))
    screen.blit(field_text, (470, 305))
