import json
import os
import shutil

DATA_FILE = "data/expenses.json"
BACKUP_DIR = "data/backup"


def load_expenses():
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as file:
                return json.load(file)
    except Exception:
        print("Error loading data.")
    return []


def save_expenses(data):
    try:
        if os.path.exists(DATA_FILE):
            os.makedirs(BACKUP_DIR, exist_ok=True)
            shutil.copy(DATA_FILE, f"{BACKUP_DIR}/backup.json")

        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)
    except Exception:
        print("Error saving data.")


def export_to_csv(expenses):
    import csv
    os.makedirs("data/exports", exist_ok=True)

    with open("data/exports/expenses.csv", "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["date", "amount", "category", "description"]
        )
        writer.writeheader()
        for e in expenses:
            writer.writerow(e)
