import csv # Импорт модуля для работы с CSV файлами
import json # Импорт модуля для работы с данными в формате JSON

# Определение констант с именами файлов
INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    data = [] # Инициализация пустого списка для хранения данных
    with open(INPUT_FILENAME, 'r') as file: # Открытие файла для чтения и сохранение в переменную
        csv_reader = csv.DictReader(file) # Создание объекта для чтения файла как словаря
        for row in csv_reader: # Перебор каждой строки
            data.append(row) # Добавление каждой строки в список

    with open(OUTPUT_FILENAME, 'w') as output_file: # Открытие файла для записи и сохранение в переменную
        json.dump(data, output_file, indent=4) # Запись списка в формате JSON с отступами, равными 4


if __name__ == '__main__': # Проверка, что скрипт запущен как отдельное приложение
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f: # Перебор каждой строки
            print(line, end="") # Вывод строки на экран с удалением символа новой строки
