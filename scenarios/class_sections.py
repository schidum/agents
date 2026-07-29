import random
import pygame


def build_question():
    students_per_section = 40
    chosen_students = 240
    correct_answer = chosen_students // students_per_section
    options = [correct_answer, correct_answer - 1, correct_answer + 1, correct_answer + 2]
    random.shuffle(options)

    return {
        "title": "Классы и ученики",
        "story": "В каждом классе учится одинаковое число детей.",
        "prompt": f"Если в одном классе {students_per_section} учеников, сколько классов нужно для {chosen_students} учеников?",
        "formula_text": f"{chosen_students} ÷ {students_per_section} = {correct_answer}",
        "correct_answer": correct_answer,
        "options": options,
        "explanation": "Больше детей — больше классов. Это прямая пропорция.",
    }


def draw_scene(screen, title_font, body_font, small_font, width, height, question):
    """Рисуем учеников в рядах."""
    pygame.draw.rect(screen, (255, 247, 214), (70, 220, 320, 220), border_radius=20)
    pygame.draw.rect(screen, (0, 0, 0), (70, 220, 320, 220), 3, border_radius=20)

    for x in [120, 220, 320]:
        pygame.draw.circle(screen, (54, 102, 208), (x, 300), 24)
        pygame.draw.rect(screen, (255, 159, 67), (x - 28, 330, 56, 40), border_radius=10)

    class_text = small_font.render("Ученики", True, (20, 20, 20))
    screen.blit(class_text, (470, 305))
