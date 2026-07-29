"""Direct Proportion Parade

A tiny educational game for children. The player helps a cheerful character
collect gems by solving simple direct-proportion questions.

The core idea is easy to understand:
- If one chest holds 2 gems, then 3 chests hold 6 gems.
- The amount grows in a straight, predictable way.

This file is intentionally simple so that children can focus on the math.
It also contains many comments to make the code easy to read for students,
teachers, and future agents that may extend the project.
"""

import random
import pygame

# ---------------------------------------------------------------------------
# Global constants
# ---------------------------------------------------------------------------

WIDTH, HEIGHT = 960, 640
FPS = 60

# A few friendly colors.
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
    """Main game object that stores state and runs the game loop."""

    def __init__(self):
        # Start pygame and create the window.
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Direct Proportion Parade")
        self.clock = pygame.time.Clock()

        # Use fonts so text is easy to read.
        self.title_font = pygame.font.SysFont("Arial", 48, bold=True)
        self.heading_font = pygame.font.SysFont("Arial", 34, bold=True)
        self.body_font = pygame.font.SysFont("Arial", 28)
        self.small_font = pygame.font.SysFont("Arial", 22)

        # Game state.
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

        # Set the first question.
        self.new_question()

    def new_question(self):
        """Create a fresh direct-proportion question and answer choices."""
        # Direct proportion means the total grows by the same amount each time.
        # For example, if 1 chest has 2 gems, then 3 chests have 6 gems.
        # We choose a simple "per box" value and a number of boxes.
        per_box = random.choice([2, 3, 4])
        box_count = random.choice([2, 3, 4, 5])
        correct_answer = per_box * box_count

        # Create three simple answer choices. The correct answer is always one of them.
        # The distractors are close enough to feel real but not correct.
        options = [correct_answer]
        if correct_answer - 2 >= 1:
            options.append(correct_answer - 2)
        else:
            options.append(correct_answer + 1)

        if correct_answer + 2 not in options:
            options.append(correct_answer + 2)
        else:
            options.append(correct_answer + 1)

        # Keep the choices unique and shuffle them so the correct answer is not always first.
        options = list(dict.fromkeys(options))
        random.shuffle(options)

        # Save the question data in a dictionary for easy drawing and checks.
        self.question = {
            "per_box": per_box,
            "box_count": box_count,
            "correct_answer": correct_answer,
            "options": options,
        }

        # Build the answer button positions.
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
        """Draw the sky, sun, and grassy ground."""
        self.screen.fill(SKY_BLUE)

        # Sun.
        pygame.draw.circle(self.screen, GOLD, (120, 120), 60)

        # Ground.
        pygame.draw.rect(self.screen, GROUND_GREEN, (0, 480, WIDTH, HEIGHT - 480))

        # A few simple clouds to make the scene feel friendly.
        for x in [180, 400, 720]:
            pygame.draw.circle(self.screen, WHITE, (x, 100), 25)
            pygame.draw.circle(self.screen, WHITE, (x + 25, 100), 25)
            pygame.draw.circle(self.screen, WHITE, (x + 50, 100), 25)

    def draw_title_screen(self):
        """Draw the opening screen and instructions."""
        self.draw_background()

        title = self.title_font.render("Direct Proportion Parade", True, BLACK)
        self.screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 70))

        subtitle = self.body_font.render("Help the little explorer collect gems!", True, BLACK)
        self.screen.blit(subtitle, (WIDTH // 2 - subtitle.get_width() // 2, 140))

        help_text = [
            "Each box holds the same number of gems.",
            "More boxes means more gems in a straight line.",
            "Click the correct answer or press 1, 2, or 3.",
        ]
        for index, text in enumerate(help_text):
            rendered = self.body_font.render(text, True, BLACK)
            y = 220 + index * 40
            self.screen.blit(rendered, (WIDTH // 2 - rendered.get_width() // 2, y))

        # Start button.
        self.start_button = pygame.Rect(WIDTH // 2 - 120, 380, 240, 70)
        pygame.draw.rect(self.screen, BUTTON_GREEN, self.start_button)
        start_text = self.heading_font.render("Start", True, WHITE)
        self.screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, 395))

    def draw_playing_screen(self):
        """Draw the question, the visual example, and the answer buttons."""
        self.draw_background()

        # Show the current score and round number.
        score_text = self.small_font.render(f"Score: {self.score}/{self.max_rounds}", True, BLACK)
        self.screen.blit(score_text, (30, 25))

        question = self.question
        if question is None:
            return

        # Explain the rule at the top.
        rule_sentence = (
            f"If 1 chest holds {question['per_box']} gems, how many gems are in "
            f"{question['box_count']} chests?"
        )
        rule_text = self.heading_font.render(rule_sentence, True, BLACK)
        self.screen.blit(rule_text, (WIDTH // 2 - rule_text.get_width() // 2, 60))

        # Show a simple formula that makes the ratio clear.
        formula = f"{question['per_box']} x {question['box_count']} = {question['correct_answer']}"
        formula_text = self.body_font.render(formula, True, PURPLE)
        self.screen.blit(formula_text, (WIDTH // 2 - formula_text.get_width() // 2, 110))

        # Draw the visual chests and gems. This is the heart of the lesson.
        chest_y = 220
        chest_width = 90
        chest_height = 80
        chest_spacing = 120
        left_margin = (WIDTH - (question['box_count'] - 1) * chest_spacing - chest_width) // 2

        for index in range(question['box_count']):
            chest_x = left_margin + index * chest_spacing
            pygame.draw.rect(self.screen, BUTTON_ORANGE, (chest_x, chest_y, chest_width, chest_height), border_radius=12)
            pygame.draw.rect(self.screen, BLACK, (chest_x, chest_y, chest_width, chest_height), 3, border_radius=12)

            # Add a lid to the chest.
            pygame.draw.rect(self.screen, BUTTON_RED, (chest_x + 10, chest_y - 16, chest_width - 20, 20), border_radius=8)

            # Draw the gems inside the chest.
            gem_count = question['per_box']
            for gem_index in range(gem_count):
                gem_x = chest_x + 20 + (gem_index % 2) * 20
                gem_y = chest_y + 20 + (gem_index // 2) * 20
                pygame.draw.circle(self.screen, GOLD, (gem_x, gem_y), 12)
                pygame.draw.circle(self.screen, BLACK, (gem_x, gem_y), 12, 2)

        # Draw the answer buttons.
        for rect, answer in self.answer_buttons:
            color = BUTTON_BLUE
            pygame.draw.rect(self.screen, color, rect, border_radius=12)
            pygame.draw.rect(self.screen, BLACK, rect, 3, border_radius=12)
            text = self.body_font.render(str(answer), True, WHITE)
            self.screen.blit(text, (rect.x + rect.width // 2 - text.get_width() // 2, rect.y + 14))

        # Show feedback if the player just answered.
        if self.feedback_text:
            feedback_surface = self.body_font.render(self.feedback_text, True, BLACK)
            self.screen.blit(feedback_surface, (WIDTH // 2 - feedback_surface.get_width() // 2, 520))

    def draw_game_over_screen(self):
        """Show the final score and a way to play again."""
        self.draw_background()

        heading = self.title_font.render("Great work!", True, BLACK)
        self.screen.blit(heading, (WIDTH // 2 - heading.get_width() // 2, 100))

        score_text = self.heading_font.render(f"You solved {self.score} out of {self.max_rounds} rounds.", True, BLACK)
        self.screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 180))

        tip_text = self.body_font.render("Direct proportion means every extra box adds the same amount.", True, BLACK)
        self.screen.blit(tip_text, (WIDTH // 2 - tip_text.get_width() // 2, 240))

        self.restart_button = pygame.Rect(WIDTH // 2 - 140, 340, 280, 70)
        pygame.draw.rect(self.screen, BUTTON_GREEN, self.restart_button)
        restart_text = self.heading_font.render("Play Again", True, WHITE)
        self.screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, 355))

    def handle_events(self):
        """Handle user input for mouse clicks and keyboard presses."""
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
        """Respond when the player picks an answer."""
        if self.question is None:
            return

        self.round += 1
        if answer == self.question["correct_answer"]:
            self.score += 1
            self.feedback_text = "Correct! Nice job!"
        else:
            self.feedback_text = f"Not quite. The right answer is {self.question['correct_answer']}."

        # Give the player a short moment to read the message before the next question.
        self.feedback_timer = pygame.time.get_ticks() + 900

        if self.round >= self.max_rounds:
            self.state = "game_over"
        else:
            self.state = "playing"

    def update(self):
        """Advance the game and move to the next question when the timer expires."""
        if self.state == "playing" and self.feedback_text:
            if pygame.time.get_ticks() >= self.feedback_timer:
                self.feedback_text = ""
                self.new_question()

    def draw(self):
        """Route each state to the correct drawing function."""
        if self.state == "title":
            self.draw_title_screen()
        elif self.state == "playing":
            self.draw_playing_screen()
        elif self.state == "game_over":
            self.draw_game_over_screen()

    def run(self):
        """Main loop for the game."""
        self.running = True
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(FPS)


def main():
    """Entry point for the game."""
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
