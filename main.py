import json
import os
from datetime import datetime

FILE = "tasks.json"


# --------- Data layer ---------
def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)


# --------- Core logic ---------
def add_task(title, category="general"):
    tasks = load_tasks()

    task = {
        "id": len(tasks) + 1,
        "title": title,
        "category": category,
        "done": False,
        "created_at": datetime.now().isoformat()
    }

    tasks.append(task)
    save_tasks(tasks)
    print(f"✔ Feladat hozzáadva: {title}")


def list_tasks(show_done=True):
    tasks = load_tasks()

    if not tasks:
        print("Nincs még feladat.")
        return

    for t in tasks:
        if not show_done and t["done"]:
            continue

        status = "✓" if t["done"] else "✗"
        print(f"{t['id']}. [{status}] {t['title']} ({t['category']})")


def complete_task(task_id):
    tasks = load_tasks()

    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True
            save_tasks(tasks)
            print(f"✔ Készre jelölve: {t['title']}")
            return

    print("Nincs ilyen ID.")


def delete_task(task_id):
    tasks = load_tasks()
    tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks(tasks)
    print("🗑 Törölve.")


# --------- CLI ---------
def menu():
    print("\n--- SelfDev Todo App ---")
    print("1. Feladat hozzáadása")
    print("2. Lista")
    print("3. Készre jelölés")
    print("4. Törlés")
    print("0. Kilépés")


def run():
    while True:
        menu()
        choice = input("Választás: ")

        if choice == "1":
            title = input("Feladat: ")
            category = input("Kategória (opcionális): ") or "general"
            add_task(title, category)

        elif choice == "2":
            list_tasks()

        elif choice == "3":
            task_id = int(input("ID: "))
            complete_task(task_id)

        elif choice == "4":
            task_id = int(input("ID: "))
            delete_task(task_id)

        elif choice == "0":
            print("Kilépés...")
            break

        else:
            print("Érvénytelen választás.")


if __name__ == "__main__":
    run()