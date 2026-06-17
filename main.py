from task_manager import TaskManager

manager = TaskManager()


def print_tasks(tasks):

    if not tasks:
        print("\nNincs találat.")
        return

    print()

    for task in tasks:

        status = "✓" if task.done else "✗"

        print(
            f"{task.id}. "
            f"[{status}] "
            f"{task.title} | "
            f"{task.priority.upper()} | "
            f"{task.category} | "
            f"{task.due_date}"
        )


while True:

    print("""
===== SELFDEV APP =====

1 - Feladat hozzáadása
2 - Feladatok listázása
3 - Feladat készre jelölése
4 - Feladat törlése
5 - Keresés
6 - Prioritás szűrés
7 - Folyamatban lévő feladatok
8 - Befejezett feladatok
0 - Kilépés
""")

    choice = input("Választás: ")

    if choice == "1":

        title = input("Cím: ")
        category = input("Kategória: ")
        priority = input(
            "Prioritás (low/medium/high): "
        )
        due_date = input(
            "Határidő (YYYY-MM-DD): "
        )

        manager.add_task(
            title=title,
            category=category,
            priority=priority,
            due_date=due_date,
        )

        print("Feladat létrehozva.")

    elif choice == "2":

        print_tasks(manager.list_tasks())

    elif choice == "3":

        task_id = int(input("ID: "))

        if manager.complete_task(task_id):
            print("Készre jelölve.")
        else:
            print("Nincs ilyen feladat.")

    elif choice == "4":

        task_id = int(input("ID: "))

        if manager.delete_task(task_id):
            print("Törölve.")
        else:
            print("Nincs ilyen feladat.")

    elif choice == "5":

        keyword = input("Keresés: ")

        print_tasks(
            manager.search_tasks(keyword)
        )

    elif choice == "6":

        priority = input(
            "Prioritás (low/medium/high): "
        )

        print_tasks(
            manager.filter_by_priority(priority)
        )

    elif choice == "7":

        print_tasks(
            manager.pending_tasks()
        )

    elif choice == "8":

        print_tasks(
            manager.completed_tasks()
        )

    elif choice == "0":
        break

    else:
        print("Érvénytelen választás.")