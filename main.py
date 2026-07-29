"""Парад прямой пропорции

Небольшая обучающая игра для детей. Игрок помогает весёлому герою
собирать самоцветы, решая простые задачи на прямую пропорцию.

Главная идея очень простая:
- Если один сундук вмещает 2 самоцвета, то 3 сундука вмещают 6 самоцветов.
- Количество растёт предсказуемо и ровно.

Этот файл намеренно прост, чтобы дети могли сосредоточиться на математике.
Он также содержит много комментариев, чтобы код был понятен ученикам,
учителям и будущим агентам, которые захотят расширить проект.
"""

import random
import pygame

# ---------------------------------------------------------------------------
# Глобальные константы
# ---------------------------------------------------------------------------

WIDTH, HEIGHT = 960, 640
FPS = 60

# Несколько дружелюбных цветов.
WHITE = (255, 255, 255)
BLACK = (20, 20, 20)
SKY_BLUE = (123, 199, 255)
GROUND_GREEN = (108, 187, 100)
BUTTON_BLUE = (54, 102, 208)
BUTTON_ORANGE = (255, 159, 67)
BUTTON_GREEN = (76, 175, 80)
BUTTON_RED = (229, 115, 115)
GOLD = (255, 215, 0)
PINK = (255, 111, 161)
PURPLE = (130, 98, 255)


class Game:
    """Основной объект игры, который хранит состояние и запускает игровой цикл."""

    def __init__(self):
        # Запускаем pygame и создаём окно.
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Парад прямой пропорции")
        self.clock = pygame.time.Clock()

        # Используем шрифты, чтобы текст был легко читаем.
        self.title_font = pygame.font.SysFont("Arial", 48, bold=True)
        self.heading_font = pygame.font.SysFont("Arial", 34, bold=True)
        self.body_font = pygame.font.SysFont("Arial", 28)
        self.small_font = pygame.font.SysFont("Arial", 22)

        # Состояние игры.
        self.state = "title"  # title -> playing -> game_over
        self.score = 0
        self.round = 0
        self.max_rounds = 8
        self.feedback_text = ""
        self.feedback_timer = 0
        self.question = None
        self.answer_buttons = []
        self.start_button = None
        self.restart_button = None

        # Готовим первый вопрос.
        self.new_question()

    def new_question(self):
        """Создаём новый вопрос на прямую пропорцию и варианты ответов."""
        # Прямая пропорция означает, что всё растёт одинаково каждый раз.
        # Например, если 1 сундук вмещает 2 самоцвета, то 3 сундука вмещают 6.
        # Мы выбираем простое значение «на один сундук» и количество сундуков.
        per_box = random.choice([2, 3, 4])
        box_count = random.choice([2, 3, 4, 5])
        correct_answer = per_box * box_count

        # Создаём три простых варианта ответа. Правильный ответ всегда есть среди них.
        # Отвлекающие варианты достаточно близки, чтобы выглядеть правдоподобно, но быть неверными.
        options = [correct_answer]
        if correct_answer - 2 >= 1:
            options.append(correct_answer - 2)
        else:
            options.append(correct_answer + 1)

        if correct_answer + 2 not in options:
            options.append(correct_answer + 2)
        else:
            options.append(correct_answer + 1)

        # Делаем варианты уникальными и перемешиваем их, чтобы правильный ответ не всегда был первым.
        options = list(dict.fromkeys(options))
        random.shuffle(options)

        # Сохраняем данные вопроса в словарь для простого рисования и проверки.
        self.question = {
            "per_box": per_box,
            "box_count": box_count,
            "correct_answer": correct_answer,
            "options": options,
        }

        # Создаём позиции кнопок ответа.
        self.answer_buttons = []
        button_y = HEIGHT - 140
        button_width = 140
        button_height = 60
        spacing = 20
        start_x = (WIDTH - (3 * button_width + 2 * spacing)) // 2

        for index, answer in enumerate(options):
            x = start_x + index * (button_width + spacing)
            rect = pygame.Rect(x, button_y, button_width, button_height)
            self.answer_buttons.append((rect, answer))

    def draw_background(self):
        """Рисуем небо, солнце и травянистую землю."""
        self.screen.fill(SKY_BLUE)

        # Солнце.
        pygame.draw.circle(self.screen, GOLD, (120, 120), 60)

        # Земля.
        pygame.draw.rect(self.screen, GROUND_GREEN, (0, 480, WIDTH, HEIGHT - 480))

        # Несколько простых облаков, чтобы сцена казалась дружелюбной.
        for x in [180, 400, 720]:
            pygame.draw.circle(self.screen, WHITE, (x, 100), 25)
            pygame.draw.circle(self.screen, WHITE, (x + 25, 100), 25)
            pygame.draw.circle(self.screen, WHITE, (x + 50, 100), 25)

    def draw_title_screen(self):
        """Рисуем стартовый экран и инструкции."""
        self.draw_background()

        title = self.title_font.render("Парад прямой пропорции", True, BLACK)
        self.screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 70))

        subtitle = self.body_font.render("Помоги маленькому исследователю собирать самоцветы!", True, BLACK)
        self.screen.blit(subtitle, (WIDTH // 2 - subtitle.get_width() // 2, 140))

        help_text = [
            "Каждый сундук вмещает одинаковое число самоцветов.",
            "Больше сундуков — больше самоцветов, и это происходит ровно.",
            "Нажми правильный ответ или используй 1, 2 или 3.",
        ]
        for index, text in enumerate(help_text):
            rendered = self.body_font.render(text, True, BLACK)
            y = 220 + index * 40
            self.screen.blit(rendered, (WIDTH // 2 - rendered.get_width() // 2, y))

        # Кнопка старта.
        self.start_button = pygame.Rect(WIDTH // 2 - 120, 380, 240, 70)
        pygame.draw.rect(self.screen, BUTTON_GREEN, self.start_button)
        start_text = self.heading_font.render("Начать", True, WHITE)
        self.screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, 395))

    def draw_playing_screen(self):
        """Рисуем вопрос, наглядный пример и кнопки ответов."""
        self.draw_background()

        # Показываем текущий счёт и номер раунда.
        score_text = self.small_font.render(f"Счёт: {self.score}/{self.max_rounds}", True, BLACK)
        self.screen.blit(score_text, (30, 25))

        question = self.question
        if question is None:
            return

        # Объясняем правило вверху.
        rule_sentence = (
            f"Если 1 сундук вмещает {question['per_box']} самоцветов, "
            f"сколько самоцветов будет в {question['box_count']} сундуках?"
        )
        rule_text = self.heading_font.render(rule_sentence, True, BLACK)
        self.screen.blit(rule_text, (WIDTH // 2 - rule_text.get_width() // 2, 60))

        # Показываем простую формулу, чтобы отношение было видно ясно.
        formula = f"{question['per_box']} x {question['box_count']} = {question['correct_answer']}"
        formula_text = self.body_font.render(formula, True, PURPLE)
        self.screen.blit(formula_text, (WIDTH // 2 - formula_text.get_width() // 2, 110))

        # Рисуем сундуки и самоцветы. Это сердце урока.
        chest_y = 220
        chest_width = 90
        chest_height = 80
        chest_spacing = 120
        left_margin = (WIDTH - (question['box_count'] - 1) * chest_spacing - chest_width) // 2

        for index in range(question['box_count']):
            chest_x = left_margin + index * chest_spacing
            pygame.draw.rect(self.screen, BUTTON_ORANGE, (chest_x, chest_y, chest_width, chest_height), border_radius=12)
            pygame.draw.rect(self.screen, BLACK, (chest_x, chest_y, chest_width, chest_height), 3, border_radius=12)

            # Добавляем крышку сундука.
            pygame.draw.rect(self.screen, BUTTON_RED, (chest_x + 10, chest_y - 16, chest_width - 20, 20), border_radius=8)

            # Рисуем самоцветы внутри сундука.
            gem_count = question['per_box']
            for gem_index in range(gem_count):
                gem_x = chest_x + 20 + (gem_index % 2) * 20
                gem_y = chest_y + 20 + (gem_index // 2) * 20
                pygame.draw.circle(self.screen, GOLD, (gem_x, gem_y), 12)
                pygame.draw.circle(self.screen, BLACK, (gem_x, gem_y), 12, 2)

        # Рисуем кнопки ответов.
        for rect, answer in self.answer_buttons:
            color = BUTTON_BLUE
            pygame.draw.rect(self.screen, color, rect, border_radius=12)
            pygame.draw.rect(self.screen, BLACK, rect, 3, border_radius=12)
            text = self.body_font.render(str(answer), True, WHITE)
            self.screen.blit(text, (rect.x + rect.width // 2 - text.get_width() // 2, rect.y + 14))

        # Показываем подсказку, если игрок только что ответил.
        if self.feedback_text:
            feedback_surface = self.body_font.render(self.feedback_text, True, BLACK)
            self.screen.blit(feedback_surface, (WIDTH // 2 - feedback_surface.get_width() // 2, 520))

    def draw_game_over_screen(self):
        """Показываем финальный счёт и возможность сыграть ещё раз."""
        self.draw_background()

        heading = self.title_font.render("Отличная работа!", True, BLACK)
        self.screen.blit(heading, (WIDTH // 2 - heading.get_width() // 2, 100))

        score_text = self.heading_font.render(f"Ты решил {self.score} из {self.max_rounds} раундов.", True, BLACK)
        self.screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 180))

        tip_text = self.body_font.render("Прямая пропорция значит, что каждый новый сундук добавляет одинаковое количество.", True, BLACK)
        self.screen.blit(tip_text, (WIDTH // 2 - tip_text.get_width() // 2, 240))

        self.restart_button = pygame.Rect(WIDTH // 2 - 140, 340, 280, 70)
        pygame.draw.rect(self.screen, BUTTON_GREEN, self.restart_button)
        restart_text = self.heading_font.render("Играть снова", True, WHITE)
        self.screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, 355))

    def handle_events(self):
        """Обрабатываем ввод пользователя: клики мышью и клавиши."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.state == "title":
                    if self.start_button and self.start_button.collidepoint(event.pos):
                        self.state = "playing"
                        self.round = 0
                        self.score = 0
                        self.feedback_text = ""
                        self.new_question()
                elif self.state == "playing":
                    for rect, answer in self.answer_buttons:
                        if rect.collidepoint(event.pos):
                            self.answer_selected(answer)
                            break
                elif self.state == "game_over":
                    if self.restart_button and self.restart_button.collidepoint(event.pos):
                        self.state = "playing"
                        self.score = 0
                        self.round = 0
                        self.feedback_text = ""
                        self.new_question()

            if event.type == pygame.KEYDOWN:
                if self.state == "title" and event.key == pygame.K_RETURN:
                    self.state = "playing"
                    self.round = 0
                    self.score = 0
                    self.feedback_text = ""
                    self.new_question()
                elif self.state == "playing":
                    if event.key == pygame.K_1:
                        self.answer_selected(self.question["options"][0])
                    elif event.key == pygame.K_2 and len(self.question["options"]) > 1:
                        self.answer_selected(self.question["options"][1])
                    elif event.key == pygame.K_3 and len(self.question["options"]) > 2:
                        self.answer_selected(self.question["options"][2])
                elif self.state == "game_over" and event.key == pygame.K_RETURN:
                    self.state = "playing"
                    self.score = 0
                    self.round = 0
                    self.feedback_text = ""
                    self.new_question()

    def answer_selected(self, answer):
        """Отвечаем, когда игрок выбирает вариант."""
        if self.question is None:
            return

        self.round += 1
        if answer == self.question["correct_answer"]:
            self.score += 1
            self.feedback_text = "Верно! Отличная работа!"
        else:
            self.feedback_text = f"Почти. Правильный ответ: {self.question['correct_answer']}."

        # Даём игроку короткую паузу, чтобы прочитать сообщение перед следующим вопросом.
        self.feedback_timer = pygame.time.get_ticks() + 900

        if self.round >= self.max_rounds:
            self.state = "game_over"
        else:
            self.state = "playing"

    def update(self):
        """Переходим к следующему вопросу, когда таймер закончился."""
        if self.state == "playing" and self.feedback_text:
            if pygame.time.get_ticks() >= self.feedback_timer:
                self.feedback_text = ""
                self.new_question()

    def draw(self):
        """Направляем каждое состояние в нужную функцию рисования."""
        if self.state == "title":
            self.draw_title_screen()
        elif self.state == "playing":
            self.draw_playing_screen()
        elif self.state == "game_over":
            self.draw_game_over_screen()

    def run(self):
        """Основной цикл игры."""
        self.running = True
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(FPS)


def main():
    """Точка входа в игру."""
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
