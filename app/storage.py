from pathlib import Path
import json


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "death_notes.json"


def load_notes():
    if not DATA_FILE.exists():
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

            if isinstance(data, list):
                return data

            return []

    except json.JSONDecodeError:
        return []


def save_notes(notes):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(notes, file, ensure_ascii=False, indent=4)