from pathlib import Path

def total_salary(path):
    total = 0
    num_devs = 0

    try:
        with open(path, 'r', encoding='utf-8') as fh:
            for line in fh:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    name, salary = parts
                    total += int(salary)
                    num_devs += 1
    
        average = int(total / num_devs if num_devs > 0 else 0)
        return total, average

    except FileNotFoundError:
        print(f"Помилка: Файл '{path}' не знайдено.")
        return None, None
    except PermissionError:
        print(f"Помилка: Немає доступу до файлу '{path}'.")
        return None, None
    except Exception as e:
        print(f"Невідома помилка: {e}")
        return None, None


total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітньої плати: {total}, Середня зарплата: {average}")


