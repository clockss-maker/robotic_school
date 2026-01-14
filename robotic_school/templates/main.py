from database import init_db
from services import *

init_db()
seed_data()

while True:
    print("""
========= МЕНЮ =========
1 - Показати студентів
2 - Додати студента
3 - Оновити студента
4 - Видалити студента
5 - Показати обладнання
6 - Додати обладнання
7 - Показати вчителів
8 - Пошук студента
9 - Список уроків
0 - Вийти
========================
""")

    ch = input("Вибір: ")

    # --------- SHOW ---------

    if ch == "1":
        for s in get_students():
            print(f"ID:{s[0]} | {s[1]} | {s[2]} клас")

    # --------- ADD ---------

    elif ch == "2":
        name = input("ПІБ студента: ")

        exist = find_student(name)
        if exist:
            print("❗ Такий студент вже існує:", exist)
            ok = input("Додати ще раз? (так/ні): ")
            if ok.lower() != "так":
                continue

        cls = input("Клас (1=10,2=11,3=12): ")

        if cls not in ["1","2","3"]:
            print("❌ Невірний клас!")
            continue

        add_student(name, cls)
        print("✔ Студента додано")

    # --------- UPDATE ---------

    elif ch == "3":
        id = input("ID: ")
        name = input("Нове ім'я: ")
        cls = input("Новий клас: ")
        update_student(id, name, cls)

    # --------- DELETE ---------

    elif ch == "4":
        id = input("ID: ")
        delete_student(id)

    # --------- EQUIPMENT ---------

    elif ch == "5":
        for e in get_equipment():
            print(f"{e[1]} - {e[2]} шт")

    elif ch == "6":
        name = input("Назва: ")
        qty = input("Кількість: ")
        add_equipment(name, qty)

    # --------- TEACHERS ---------

    elif ch == "7":
        for t in get_teachers():
            print(f"{t[1]} - {t[2]}")

    # --------- SEARCH ---------

    elif ch == "8":
        key = input("Введи ім'я: ")
        res = search_student(key)

        if not res:
            print("❌ Студента не знайдено")

        for s in res:
            print(f"{s[1]} | {s[2]} клас")

    # --------- LESSONS ---------

    elif ch == "9":
        for l in get_lessons():
            print(l[1])

    elif ch == "0":
        print("Вихід...")
        break
