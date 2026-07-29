# Direct Proportion Parade

Direct Proportion Parade is a small pygame game made for children who are learning how direct proportion works. The player helps a cheerful explorer collect gems by choosing the correct answer to simple questions such as:

- If 1 chest holds 2 gems, how many gems are in 3 chests?
- If 1 box holds 3 cookies, how many cookies are in 4 boxes?

The game keeps the experience gentle and visual. Each round shows a clear example with chests and gems so the child can see that the total grows in a steady way.

## Features

- Very simple one-screen game loop
- Friendly visuals and bright colors
- Clear direct-proportion questions
- Keyboard or mouse play
- Built with only pygame and Python standard library

## Installation

1. Open a terminal in this project folder.
2. Create and activate a virtual environment:
   - Windows PowerShell: `python -m venv .venv` then `.venv\Scripts\Activate.ps1`
3. Install the dependency:
   - `python -m pip install -r requirements.txt`
4. Run the game:
   - `python main.py`

## How to play

- Press Enter or click Start to begin.
- Read the question and look at the chests and gems.
- Click the correct answer button or press 1, 2, or 3 on the keyboard.
- After each round, the game gives a short message and then presents a new question.
- After 8 rounds, the game shows your score.

## Project layout

- `main.py` - the full game implementation
- `requirements.txt` - python dependencies
- `README.md` - overview and setup instructions
- `CONTRIBUTING.md` - how to contribute safely
- `DEVELOPMENT.md` - local workflow and testing notes
- `.github/copilot-instructions.md` - guidance for agentic development

## Agentic development notes

This repository is intentionally simple so that future agents can extend it safely. The game logic is centered in `main.py`, and the project docs explain the intended learning goal and coding style.
