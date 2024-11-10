# TODO решите задачу
import json


def task() -> float:
    with open("input.json", 'r') as file:
        data = json.load(file)

    total = 0
    for item in data:
        product = item["score"] * item["weight"]
        total += product

    return round(total, 3)


print(task())
