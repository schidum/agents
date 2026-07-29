import random
import pygame


def build_question():
    machines = 2
    units_per_machine = 10
    chosen_machines = 4
    correct_answer = units_per_machine * chosen_machines
    options = [correct_answer, correct_answer - 10, correct_answer + 10, correct_answer + 20]
    random.shuffle(options)

    return {
        "title": "Производство на фабрике",
        "story": "Каждая машина делает одинаковое число вещей за день.",
        "prompt": f"Если {machines} машины делают {units_per_machine * machines} вещей, сколько вещей сделают {chosen_machines} машины?",
        "correct_answer": correct_answer,
        "options": options,
        "explanation": "Больше машин — больше изделий. Это прямая пропорция.",
    }


def draw_scene(screen, title_font, body_font, small_font, width, height, question):
    """Рисуем две машины и коробки."""
    pygame.draw.rect(screen, (255, 247, 214), (70, 220, 320, 220), border_radius=20)
    pygame.draw.rect(screen, (0, 0, 0), (70, 220, 320, 220), 3, border_radius=20)

    for x in [140, 260]:
        pygame.draw.rect(screen, (54, 102, 208), (x, 290, 70, 60), border_radius=10)
        pygame.draw.rect(screen, (255, 255, 255), (x + 12, 300, 40, 25), border_radius=6)
        pygame.draw.rect(screen, (255, 159, 67), (x + 20, 270, 30, 20), border_radius=8)

    pygame.draw.rect(screen, (76, 175, 80), (430, 285, 80, 70), border_radius=10)
    pygame.draw.rect(screen, (255, 255, 255), (445, 300, 50, 35), border_radius=6)

    machine_text = small_font.render("Машины", True, (20, 20, 20))
    screen.blit(machine_text, (470, 365))
