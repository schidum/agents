# Agentic development guide

This project is designed to be easy for both humans and coding agents to extend.

## What to preserve

- The game should stay simple enough for a school child.
- The direct-proportion lesson should remain clear.
- Comments should explain the educational logic, not just the code mechanics.
- Each scenario module should stay small and focused on one example.

## Safe change strategy

- Start with a small change in `main.py` or one module in `scenarios/`.
- Keep the UI calm and readable.
- Prefer adding another real-life scenario over redesigning the whole game.
- Update the README when the player experience changes.

## Helpful commands

```bash
python -m pip install -r requirements.txt
python main.py
```

## Good agent habits

- Read existing code before editing.
- Use the smallest change that solves the problem.
- Keep the project child-friendly and educational.
- When adding a new scenario, make sure the math is easy to follow and the visual is simple.
