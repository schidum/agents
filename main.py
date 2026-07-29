import random
import pygame

from scenarios import SCENARIO_MODULES

WIDTH, HEIGHT = 960, 640
FPS = 60

WHITE = (255, 255, 255)
BLACK = (20, 20, 20)
SKY_BLUE = (123, 199, 255)
GROUND_GREEN = (108, 187, 100)
BUTTON_BLUE = (54, 102, 208)
BUTTON_ORANGE = (255, 159, 67)
BUTTON_GREEN = (76, 175, 80)
BUTTON_RED = (229, 115, 115)
GOLD = (255, 215, 0)
PURPLE = (130, 98, 255)


class Game:
    """Основной объект игры. Здесь хранится состояние и логика раундов."""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Парад прямой пропорции")
        self.clock = pygame.time.Clock()

        self.title_font = pygame.font.SysFont("Arial", 48, bold=True)
        self.heading_font = pygame.font.SysFont("Arial", 34, bold=True)
        self.body_font = pygame.font.SysFont("Arial", 28)
        self.small_font = pygame.font.SysFont("Arial", 22)

        self.state = "title"
        self.score = 0
        self.round = 0
        self.max_rounds = 10
        self.feedback_text = ""
        self.feedback_timer = 0
        self.question = None
        self.answer_buttons = []
        self.start_button = None
        self.restart_button = None
        self.current_scenario = None

        self.new_question()

    def new_question(self):
        """Выбираем новый сценарий и создаём для него вопрос."""
        module = random.choice(SCENARIO_MODULES)
        self.current_scenario = module
        self.question = module.build_question()

        self.answer_buttons = []
        button_width = 180
        button_height = 60
        gap = 20
        start_x = (WIDTH - (2 * button_width + gap)) // 2
        start_y = HEIGHT - 150

        for index, answer in enumerate(self.question["options"]):
            row = index // 2
            col = index % 2
            x = start_x + col * (button_width + gap)
            y = start_y + row * (button_height + gap)
            rect = pygame.Rect(x, y, button_width, button_height)
            self.answer_buttons.append((rect, answer))

    def draw_background(self):
        """Рисуем дружелюбный фон с небом, солнцем и землёй."""
        self.screen.fill(SKY_BLUE)
        pygame.draw.circle(self.screen, GOLD, (120, 120), 60)
        pygame.draw.rect(self.screen, GROUND_GREEN, (0, 480, WIDTH, HEIGHT - 480))

        for x in [180, 400, 720]:
            pygame.draw.circle(self.screen, WHITE, (x, 100), 25)
            pygame.draw.circle(self.screen, WHITE, (x + 25, 100), 25)
            pygame.draw.circle(self.screen, WHITE, (x + 50, 100), 25)

    def draw_title_screen(self):
        """Рисуем стартовый экран с новой идеей игры."""
        self.draw_background()
        title = self.title_font.render("Парад прямой пропорции", True, BLACK)
        self.screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 70))

        subtitle = self.body_font.render("Теперь каждый раунд — новый пример из жизни!", True, BLACK)
        self.screen.blit(subtitle, (WIDTH // 2 - subtitle.get_width() // 2, 140))

        help_text = [
            "Мы учимся на примерах из повседневной жизни.",
            "Смотрите, как одна и та же идея встречается в магазине, в школе и в дороге.",
            "Нажмите правильный ответ или используйте 1, 2, 3, 4.",
        ]
        for index, text in enumerate(help_text):
            rendered = self.body_font.render(text, True, BLACK)
            y = 210 + index * 44
            self.screen.blit(rendered, (WIDTH // 2 - rendered.get_width() // 2, y))

        self.start_button = pygame.Rect(WIDTH // 2 - 120, 380, 240, 70)
        pygame.draw.rect(self.screen, BUTTON_GREEN, self.start_button)
        start_text = self.heading_font.render("Начать", True, WHITE)
        self.screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, 395))

    def draw_playing_screen(self):
        """Рисуем вопрос, сцену и кнопки ответов."""
        self.draw_background()

        score_text = self.small_font.render(f"Счёт: {self.score}/{self.max_rounds}", True, BLACK)
        self.screen.blit(score_text, (30, 25))

        if self.question is None:
            return

        title_text = self.heading_font.render(self.question["title"], True, BLACK)
        self.screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 60))

        story_text = self.body_font.render(self.question["story"], True, BLACK)
        self.screen.blit(story_text, (WIDTH // 2 - story_text.get_width() // 2, 105))

        prompt_text = self.heading_font.render(self.question["prompt"], True, BLACK)
        self.screen.blit(prompt_text, (WIDTH // 2 - prompt_text.get_width() // 2, 145))

        formula_text = self.body_font.render(self.question["formula_text"], True, PURPLE)
        self.screen.blit(formula_text, (WIDTH // 2 - formula_text.get_width() // 2, 185))

        if self.current_scenario is not None:
            self.current_scenario.draw_scene(
                self.screen,
                self.title_font,
                self.body_font,
                self.small_font,
                WIDTH,
                HEIGHT,
                self.question,
            )

        for rect, answer in self.answer_buttons:
            pygame.draw.rect(self.screen, BUTTON_BLUE, rect, border_radius=12)
            pygame.draw.rect(self.screen, BLACK, rect, 3, border_radius=12)
            text = self.body_font.render(str(answer), True, WHITE)
            self.screen.blit(text, (rect.x + rect.width // 2 - text.get_width() // 2, rect.y + 14))

        if self.feedback_text:
            feedback_surface = self.body_font.render(self.feedback_text, True, BLACK)
            self.screen.blit(feedback_surface, (WIDTH // 2 - feedback_surface.get_width() // 2, 500))

    def draw_game_over_screen(self):
        """Показываем финальный результат и возможность сыграть ещё раз."""
        self.draw_background()
        heading = self.title_font.render("Отличная работа!", True, BLACK)
        self.screen.blit(heading, (WIDTH // 2 - heading.get_width() // 2, 100))

        score_text = self.heading_font.render(f"Ты решил {self.score} из {self.max_rounds} раундов.", True, BLACK)
        self.screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 180))

        tip_text = self.body_font.render("Прямая пропорция — это когда всё растёт или уменьшается вместе.", True, BLACK)
        self.screen.blit(tip_text, (WIDTH // 2 - tip_text.get_width() // 2, 240))

        self.restart_button = pygame.Rect(WIDTH // 2 - 140, 340, 280, 70)
        pygame.draw.rect(self.screen, BUTTON_GREEN, self.restart_button)
        restart_text = self.heading_font.render("Играть снова", True, WHITE)
        self.screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, 355))

    def handle_events(self):
        """Обрабатываем клики мышью и клавиши."""
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
                    elif event.key == pygame.K_4 and len(self.question["options"]) > 3:
                        self.answer_selected(self.question["options"][3])
                elif self.state == "game_over" and event.key == pygame.K_RETURN:
                    self.state = "playing"
                    self.score = 0
                    self.round = 0
                    self.feedback_text = ""
                    self.new_question()

    def answer_selected(self, answer):
        """Проверяем ответ игрока и готовим следующий раунд."""
        if self.question is None:
            return

        self.round += 1
        if answer == self.question["correct_answer"]:
            self.score += 1
            self.feedback_text = "Верно! Ты справился!"
        else:
            self.feedback_text = f"Почти. Правильный ответ: {self.question['correct_answer']}."

        self.feedback_timer = pygame.time.get_ticks() + 900

        if self.round >= self.max_rounds:
            self.state = "game_over"
        else:
            self.state = "playing"

    def update(self):
        """Через короткую паузу показываем новый вопрос."""
        if self.state == "playing" and self.feedback_text:
            if pygame.time.get_ticks() >= self.feedback_timer:
                self.feedback_text = ""
                self.new_question()

    def draw(self):
        """Выбираем нужный экран в зависимости от состояния."""
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
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
