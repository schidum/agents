import random
import pygame


def build_question():
    people = 20
    chapatis_per_person = 4
    new_people = 25
    correct_answer = chapatis_per_person * new_people
    options = [correct_answer, correct_answer - 20, correct_answer + 20, correct_answer + 40]
    random.shuffle(options)

    return {
        "title": "Пища в общежитии",
        "story": "Каждый живущий в общежитии съедает одинаковое число лепёшек.",
        "prompt": f"Если {people} человек едят {chapatis_per_person * people} лепёшек, сколько лепёшек нужно для {new_people} человек?",
        "formula_text": f"{chapatis_per_person} x {new_people} = {correct_answer}",
        "correct_answer": correct_answer,
        "options": options,
        "explanation": "Больше людей — больше еды. Это прямая пропорция.",
    }


def draw_scene(screen, title_font, body_font, small_font, width, height, question):
    """Рисуем тарелки и лепёшки."""
    pygame.draw.rect(screen, (255, 247, 214), (70, 220, 320, 220), border_radius=20)
    pygame.draw.rect(screen, (0, 0, 0), (70, 220, 320, 220), 3, border_radius=20)

    for x in [120, 220, 320]:
        pygame.draw.circle(screen, (255, 255, 255), (x, 310), 38)
        pygame.draw.circle(screen, (255, 255, 255), (x, 310), 24)
        pygame.draw.rect(screen, (255, 159, 67), (x - 25, 335, 50, 15), border_radius=8)

    food_text = small_font.render("Тарелки", True, (20, 20, 20))
    screen.blit(food_text, (470, 305))
