# Development guide

## Running the game

```bash
python -m pip install -r requirements.txt
python main.py
```

## Recommended checks

Because this project is a simple pygame app, the most important validation is to run the game manually and confirm that:

- the title screen appears,
- the questions load,
- answer buttons work,
- the score updates correctly,
- the game ends after 8 rounds.

## Headless smoke check

If you need to check that the app starts without a visible display, you can use a dummy video driver:

```bash
set SDL_VIDEODRIVER=dummy
python main.py
```

This is useful for CI or remote environments.

## Notes for future agents

- Keep educational content accurate and child-friendly.
- Use comments to explain why the math is being shown in a certain way.
- When you add new question types, make sure the direct-proportion relationship is still obvious.
