import random
import pygame


def build_question():
    questions_per_hour = 10
    chosen_questions = 30
    correct_answer = questions_per_hour * chosen_questions // 10
    options = [correct_answer, correct_answer - 1, correct_answer + 1, correct_answer + 2]
    random.shuffle(options)

    return {
        "title": "Домашняя работа",
        "story": "Каждую минуту ученик решает одинаковое число примеров.",
        "prompt": f"Если за 1 час он решает {questions_per_hour} примеров, сколько он решит за {chosen_questions // 10} часа?",
        "formula_text": f"{questions_per_hour} x {chosen_questions // 10} = {correct_answer}",
        "correct_answer": correct_answer,
        "options": options,
        "explanation": "Больше заданий — больше времени. Это прямая пропорция.",
    }


def draw_scene(screen, title_font, body_font, small_font, width, height, question):
    """Рисуем тетрадь и карандаш."""
    pygame.draw.rect(screen, (255, 247, 214), (70, 220, 320, 220), border_radius=20)
    pygame.draw.rect(screen, (0, 0, 0), (70, 220, 320, 220), 3, border_radius=20)

    pygame.draw.rect(screen, (255, 255, 255), (120, 260, 140, 160), border_radius=10)
    pygame.draw.rect(screen, (0, 0, 0), (120, 260, 140, 160), 3, border_radius=10)
    for y in [290, 320, 350]:
        pygame.draw.line(screen, (54, 102, 208), (140, y), (240, y), 3)

    pygame.draw.rect(screen, (255, 159, 67), (280, 310, 80, 18), border_radius=8)
    pygame.draw.rect(screen, (229, 115, 115), (300, 280, 18, 60), border_radius=6)

    homework_text = small_font.render("Тетрадь", True, (20, 20, 20))
    screen.blit(homework_text, (470, 305))
