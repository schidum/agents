import random
import pygame


def build_question():
    oranges_per_box = 10
    chosen_oranges = 30
    correct_answer = chosen_oranges // oranges_per_box
    options = [correct_answer, correct_answer - 1, correct_answer + 1, correct_answer + 2]
    random.shuffle(options)

    return {
        "title": "Хранение апельсинов",
        "story": "Каждая коробка вмещает одинаковое число апельсинов.",
        "prompt": f"Если 1 коробка вмещает {oranges_per_box} апельсинов, сколько коробок нужно для {chosen_oranges} апельсинов?",
        "formula_text": f"{chosen_oranges} ÷ {oranges_per_box} = {correct_answer}",
        "correct_answer": correct_answer,
        "options": options,
        "explanation": "Больше апельсинов — больше коробок. Это прямая пропорция.",
    }


def draw_scene(screen, title_font, body_font, small_font, width, height, question):
    """Рисуем коробки и апельсины."""
    pygame.draw.rect(screen, (255, 247, 214), (70, 220, 320, 220), border_radius=20)
    pygame.draw.rect(screen, (0, 0, 0), (70, 220, 320, 220), 3, border_radius=20)

    for x in [120, 220, 320]:
        pygame.draw.rect(screen, (255, 159, 67), (x, 280, 70, 90), border_radius=10)
        pygame.draw.rect(screen, (229, 115, 115), (x + 10, 265, 50, 20), border_radius=8)
        pygame.draw.circle(screen, (255, 215, 0), (x + 35, 315), 16)

    boxes_text = small_font.render("Коробки", True, (20, 20, 20))
    screen.blit(boxes_text, (470, 305))
