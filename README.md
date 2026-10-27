# RPG Battle Game

A small browser RPG battle built with Django.

## Run locally (Windows PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/

## Gameplay
- Attack the monster with a sword
- Use poison for a stronger special attack
- View the battle log
- Restart the battle after victory or defeat

This starter game stores the current battle state in the user's Django session.
