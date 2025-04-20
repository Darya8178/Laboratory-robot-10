try:
    name = input("Запишіть своє прізвище у файл: ").strip()
    if not name:
        raise ValueError("Прізвище не може бути порожнім!")

    task = input("Запишіть питання на тему програмування Python: ").strip()
    if not task:
        raise ValueError("Питання не може бути порожнім!")

    with open('text.txt', 'w') as file:
        file.write(f"Прізвище: {name}\n")
        file.write(f"Питання: {task}\n")

    print("Дані успішно записані у файл 'text.txt'!")

except ValueError as ve:
    print(f"Помилка вводу: {ve}")
except Exception as e:
    print(f"Сталася помилка: {e}")

