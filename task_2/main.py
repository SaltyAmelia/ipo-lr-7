#Мигунов
import json

print("start code ...")

with open("dump.json", "r", encoding="utf-8") as file:
    content = json.load(file)

search_val = input("Введите номер квалификации: ")

result_list = []

for item in content:
    if item["model"] == "data.skill":
        code = item["fields"]["code"]
        name = item["fields"]["title"]
        
        if code == search_val or code.startswith(search_val + "."):
            result_list.append([code, name])

result_list.sort()

if len(result_list) > 0:
    print("=============== Найдено ===============")
    for element in result_list:
        print(f"{element[0]} >> {element[1]}")
else:
    print("=============== Не найдено ===============")

print("... end code")
