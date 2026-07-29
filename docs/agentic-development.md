# Agentic development guide

This project is designed to be easy for both humans and coding agents to extend.

## What to preserve

- The game should stay simple enough for a school child.
- The direct-proportion lesson should remain clear.
- Comments should explain the educational logic, not just the code mechanics.

## Safe change strategy

- Start with a small change in `main.py`.
- Keep the UI calm and readable.
- Prefer adding a new question pattern over redesigning the whole game.
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
