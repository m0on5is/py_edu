list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

total_players = len(list_players)
middle_index = total_players // 2

first_team = list_players[:middle_index]
second_team = list_players[middle_index:]

print(first_team)
print(second_team)
