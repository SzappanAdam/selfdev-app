from app.services.task_manager import TaskManager

manager = TaskManager()

from fastapi import FastAPI

from app.api.routes import (
    tasks,
    habits,
    goals,
    analytics,
    charts,
    auth,
    dashboard,
    insights,
    review,
    root
)

app = FastAPI()

app.include_router(tasks.router)
app.include_router(habits.router)
app.include_router(goals.router)
app.include_router(analytics.router)
app.include_router(charts.router)
app.include_router(auth.router)
app.include_router(dashboard.router)
app.include_router(insights.router)
app.include_router(review.router)
app.include_router(root.router)

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


def main():

    while True:

        print("""
===== SELFDEV APP =====

1 - Feladat hozzáadása
2 - Összes feladat
3 - Készre jelölés
4 - Törlés
5 - Keresés
6 - Prioritás szerinti szűrés
7 - Folyamatban lévők
8 - Befejezettek
0 - Kilépés
""")

        choice = input("Választás: ")

        if choice == "1":

            title = input("Cím: ")
            category = input("Kategória: ")
            priority = input("Prioritás (low/medium/high): ")
            due_date = input("Határidő (YYYY-MM-DD): ")

            try:
                manager.add_task(
                    title,
                    category,
                    priority,
                    due_date
                )
                print("Feladat létrehozva.")

            except Exception as e:
                print(f"Hiba: {e}")

        elif choice == "2":
            print_tasks(manager.list_tasks())

        elif choice == "3":
            task_id = int(input("ID: "))

            task = manager.repo.get_task(task_id)

            if task:
                task.done = True
                manager.repo.db.commit()
                print("Készre jelölve.")
            else:
                print("Nincs ilyen task.")

        elif choice == "4":
            task_id = int(input("ID: "))
            manager.delete_task(task_id)

        elif choice == "5":
            keyword = input("Kulcsszó: ")
            print_tasks(manager.search_tasks(keyword))

        elif choice == "6":
            priority = input("Prioritás: ")
            print_tasks(manager.filter_by_priority(priority))

        elif choice == "7":
            print_tasks(manager.pending_tasks())

        elif choice == "8":
            print_tasks(manager.completed_tasks())

        elif choice == "0":
            break


if __name__ == "__main__":
    main()