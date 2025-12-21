#Мигунов Матвей, Вариант 3
import json
import os

FILENAME = "stars.json"

def load_stars():
    if not os.path.exists(FILENAME):
        return []
    
    with open(FILENAME, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            return data
        except:
            print("Не удалось прочитать файл!")
            return []

def save_stars(stars):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(stars, f, ensure_ascii=False, indent=4)

def show_all(stars):
    print("\n============== Все записи ==============")
    if len(stars) == 0:
        print("Нет записей.")
        return
    
    for s in stars:
        visible = "видна" if s["is_visible"] else "не видна"
        print(f"ID: {s['id']}")
        print(f"Название: {s['name']}")
        print(f"Созвездие: {s['constellation']}")
        print(f"Видимость: {visible} без телескопа")
        print(f"Радиус: {s['radius']} солнечных")
        print("-" * 40)

def find_by_id(stars):
    try:
        search_id = int(input("Введите ID звезды: "))
    except:
        print("ID должен быть числом!")
        return
    
    position = 0
    found = False
    
    for i in range(len(stars)):
        if stars[i]["id"] == search_id:
            position = i + 1
            star = stars[i]
            found = True
            break
    
    if found:
        print(f"\n============== Найдено ==============")
        print(f"Позиция в списке: {position}")
        visible = "видна" if star["is_visible"] else "не видна"
        print(f"ID: {star['id']}")
        print(f"Название: {star['name']}")
        print(f"Созвездие: {star['constellation']}")
        print(f"Видимость: {visible} без телескопа")
        print(f"Радиус: {star['radius']} солнечных")
    else:
        print("\n============== Не найдено ===============")

def add_new_star(stars):
    new_id = 1
    if len(stars) > 0:
        max_id = 0
        for s in stars:
            if s["id"] > max_id:
                max_id = s["id"]
        new_id = max_id + 1
    
    name = input("Введите название звезды: ").strip()
    while name == "":
        print("Название не может быть пустым!")
        name = input("Введите название звезды: ").strip()
    
    constellation = input("Введите созвездие: ").strip()
    while constellation == "":
        print("Созвездие не может быть пустым!")
        constellation = input("Введите созвездие: ").strip()
    
    is_visible = None
    while is_visible is None:
        vis_input = input("Видна без телескопа? (да/нет): ").strip().lower()
        if vis_input in ["да", "yes", "y", "1"]:
            is_visible = True
        elif vis_input in ["нет", "no", "n", "0"]:
            is_visible = False
        else:
            print("Введите 'да' или 'нет'!")
    
    radius = None
    while radius is None:
        try:
            r = float(input("Введите радиус в солнечных радиусах: "))
            if r <= 0:
                print("Радиус должен быть больше нуля!")
            else:
                radius = r
        except:
            print("Введите корректное число!")
    
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

def delete_by_id(stars):
    try:
        del_id = int(input("Введите ID звезды для удаления: "))
    except:
        print("ID должен быть числом!")
        return
    
    found = False
    new_list = []
    
    for s in stars:
        if s["id"] == del_id:
            found = True
        else:
            new_list.append(s)
    
    if found:
        stars.clear()
        for s in new_list:
            stars.append(s)
        save_stars(stars)
        print("Запись успешно удалена.")
    else:
        print("\n============== Не найдено ===============")

def main():
    print("start code ...")
    stars = load_stars()
    operations = 0
    
    while True:
        print("\nМеню:")
        print("1. Вывести все записи")
        print("2. Вывести запись по полю id")
        print("3. Добавить запись")
        print("4. Удалить запись по полю id")
        print("5. Выйти из программы")
        
        choice = input("Выберите пункт меню (1-5): ").strip()
        
        if choice == "1":
            show_all(stars)
            operations = operations + 1
        elif choice == "2":
            find_by_id(stars)
            operations = operations + 1
        elif choice == "3":
            add_new_star(stars)
            operations = operations + 1
        elif choice == "4":
            delete_by_id(stars)
            operations = operations + 1
        elif choice == "5":
            print(f"\nВыполнено операций: {operations}")
            print("... end code")
            break
        else:
            print("Некорректный выбор. Пожалуйста, введите число от 1 до 5.")

main()
