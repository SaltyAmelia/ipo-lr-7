#Мигунов Матвей, Вариант 3
import json
import os

FILENAME = "stars.json"


def load_stars():
    if os.path.exists(FILENAME):

        try:
          with open(FILENAME, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Ошибка при загрузке данных: {e}")
            return []
    return []


def save_stars(stars):
    try:
        with open(FILENAME, "w", encoding="utf-8") as f:
            json.dump(stars, f, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"Ошибка при сохранении данных: {e}")
        
def input_str(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Ошибка: поле не может быть пустым.")


def input_bool(prompt):
    while True:
        value = input(prompt).strip().lower()
        if value in ("да", "yes", "y", "1"):
            return True
        elif value in ("нет", "no", "n", "0"):
            return False
        else:
            print("Ошибка: введите 'да'/'нет' (или эквивалент: yes/no, y/n, 1/0).")


def input_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Ошибка: радиус должен быть положительным числом.")
                continue
            return value
            
        except ValueError as e:
            print("Ошибка: введите корректное число.")
def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
                
        except ValueError:
            print("Ошибка: введите целое число.")


def display_all_stars(stars):
    print("\n============== Все записи ==============")
    if not stars:
        print("Нет записей.")
    else:
        for star in stars:
            visible_str = "видна без телескопа" if star["is_visible"] else "не видна без телескопа"
            print(f"ID: {star['id']}")
            print(f"Название: {star['name']}")
            print(f"Созвездие: {star['constellation']}")
            print(f"Видимость: {visible_str}")
            print(f"Радиус (в солнечных): {star['radius']}")
            print("-" * 40)


def display_star_by_id(stars):
    target_id = input_int("Введите ID звезды: ")
    for index, star in enumerate(stars):
        if star["id"] == target_id:
            print(f"\n============== Найдено ==============")
            print(f"Позиция в списке: {index + 1}")
            visible_str = "видна без телескопа" if star["is_visible"] else "не видна без телескопа"
            print(f"ID: {star['id']}")
            print(f"Название: {star['name']}")
            print(f"Созвездие: {star['constellation']}")
            print(f"Видимость: {visible_str}")
            print(f"Радиус (в солнечных): {star['radius']}")
            return True
    print("\n============== Не найдено ===============")
    return False

def add_star(stars):
    new_id = max([s["id"] for s in stars], default=0) + 1
    name = input_str("Введите название звезды: ")
    constellation = input_str("Введите созвездие: ")
    is_visible = input_bool("Видна без телескопа? (да/нет): ")
    radius = input_positive_float("Введите радиус в солнечных радиусах: ")
    new_star = {
        "id": new_id,
        "name": name,
        "constellation": constellation,
        "is_visible": is_visible,
        "radius": radius
    }
    stars.append(new_star)
    save_stars(stars)
    print("Запись успешно добавлена.")

def delete_star(stars):
    target_id = input_int("Введите ID звезды для удаления: ")
    initial_len = len(stars)
    stars[:] = [s for s in stars if s["id"] != target_id]
    if len(stars) == initial_len:
        print("\n============== Не найдено ===============")
        return False
    else:
        save_stars(stars)
        print("Запись успешно удалена.")
        return True


def main():
    print("start code ...")
    stars = load_stars()
    operation_count = 0

    while True:
        print("\nМеню:")
        print("1. Вывести все записи")
        print("2. Вывести запись по полю id")
        print("3. Добавить запись")
        print("4. Удалить запись по полю id")
        print("5. Выйти из программы")

        choice = input("Выберите пункт меню (1-5): ").strip()

        if choice == "1":
            display_all_stars(stars)
            operation_count += 1
        elif choice == "2":
            display_star_by_id(stars)
            operation_count += 1
        elif choice == "3":
            add_star(stars)
            operation_count += 1
        elif choice == "4":
            delete_star(stars)
            operation_count += 1
        elif choice == "5":
            print(f"\nВыполнено операций: {operation_count}")
            print("... end code")
            break
        else:
            print("Некорректный выбор. Пожалуйста, введите число от 1 до 5.")


if __name__ == "__main__":
    main()