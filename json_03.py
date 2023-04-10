import json

data = {
    "president": {
        "name": "Бобёр Всемогущий",
        "age": 18
    }
}

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file)


with open("data.json", "r", encoding="utf-8") as file:
    new_data = json.load(file)

print(new_data)
