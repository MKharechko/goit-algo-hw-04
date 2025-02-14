from pathlib import Path

def get_cats_info(path):

    cats_data = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    id, name, age = parts
                    cats_data.append({"id": id, "name":name, "age":age})
        return cats_data

    except FileNotFoundError:
        print(f"Помилка: Файл '{path}' не знайдено.")
        return []
    except PermissionError:
        print(f"Помилка: Немає доступу до файлу '{path}'.")
        return []
    except Exception as e:
        print(f"Невідома помилка: {e}")
        return []

cats_info = get_cats_info("path/cats.txt")
print(*cats_info, sep="\n")