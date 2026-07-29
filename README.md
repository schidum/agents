# Direct Proportion Parade

Direct Proportion Parade is a small pygame game made for children who are learning how direct proportion works. The player helps a cheerful explorer collect gems by choosing the correct answer to simple questions from real-life situations.

The new version uses ten short examples from everyday life, such as:

- wages for a worker
- the cost of fruit
- homework time
- fuel consumption in a car
- the number of boxes needed for oranges
- food in a hostel
- goods made by machines
- students and school sections
- crop harvest on a field
- shop earnings

Each round shows one story, one simple math question, and a tiny picture so the child can see that the total grows in a steady way.

## Features

- Ten different real-life examples of direct proportion
- One small module for each example in the `scenarios` package
- Friendly visuals and bright colors
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
- Read the short story and look at the picture.
- Click the correct answer button or press 1, 2, 3, or 4 on the keyboard.
- After each round, the game gives a short message and then shows a new example.
- After 10 rounds, the game shows your score.

## Project layout

- `main.py` - the main game loop and question flow
- `scenarios/` - one Python module for each real-life example
- `requirements.txt` - Python dependencies
- `README.md` - overview and setup instructions
- `CONTRIBUTING.md` - how to contribute safely
- `DEVELOPMENT.md` - local workflow and testing notes
- `.github/copilot-instructions.md` - guidance for agentic development

## Agentic development notes

This repository is intentionally simple so that future agents can extend it safely. The educational goal stays in the foreground, and the scenario modules make it easy to add more real-life examples later.
